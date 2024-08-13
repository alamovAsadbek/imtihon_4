import hashlib
import random
import re
import threading
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.email_sender import EmailSender
from main_files.json_manager import user_manager


class StudentMenu:
    def __init__(self):
        self.__admin_email = 'alamovasad@gmail.com'
        self.__created_data = datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()

    # this function is show all students
    @log_decorator
    def show_all_students(self):
        all_students: dict = user_manager.read()
        count = 1
        for student in all_students.values():
            if student['role'] == 'student':
                yield (
                    f"{count}. ID: {student['id']}, Fullname: {student['full_name']}, Username: {student['username']}, "
                    f"Age: {student['age']}, Email: {student['email']}, Phone number: {student['phone_number']}, "
                    f"Gender: {student['gender']}, Role: {student['role']}, XP: {student['xp']} "
                    f"Created: {student['create_date']}")
                count += 1
        if count == 1:
            print("Student is not found")
            return False
        return True

    # this function is add student
    @log_decorator
    def add_student(self, update_date: int = None) -> bool:
        email_sender = EmailSender()
        fullname: str = input('Full name: ').strip()
        while len(fullname) < 3:
            print('Full name must be at least 3 characters.')
            fullname = input('Full name: ').strip()
        while True:
            if update_date is not None:
                random_username = update_date['username']
                break
            random_number: int = random.randint(1, 10000)
            name: str = fullname.split()[0]
            name = re.sub('[^A-Za-z]+', '', name)
            random_username: str = f'student_{name.lower()}_{random_number}'
            if user_manager.check_data_by_key(key='username', value=random_username):
                continue
            break

        while True:
            email: str = input('Email: ').strip()
            if update_date is not None and email == update_date['email']:
                break
            elif not user_manager.is_email_valid(email=email):
                print("Email validation failed, please try again.")
                print("Example: email@gmail.com")
                continue
            elif user_manager.check_data_by_key(key='email', value=email) or email == self.__admin_email:
                print("This email is already registered.")
                continue
            break
        age: int = int(input('Age: ').strip())
        while age < 5:
            print("The number entered must be older than 5 years")
            age: int = int(input('Age: ').strip())
        gender: str = 'male'
        while True:
            print("Choose gender")
            print(f'1. Male \t 2. Female')
            choice_gender: int = int(input('Gender: ').strip())
            if choice_gender < 1 or choice_gender > 2:
                print("Gender must be between 1 and 2.")
                continue
            elif choice_gender == 1:
                gender = 'male'
                break
            elif choice_gender == 2:
                gender = 'female'
                break
            else:
                print("Something went wrong.")

        while True:
            phone_number: str = input('Phone number (+998): ').strip()
            if update_date is not None and phone_number == update_date['phone_number']:
                break
            elif user_manager.check_data_by_key(key='phone_number', value=phone_number):
                print("This phone number is already in use.")
                continue
            break
        random_password: int = random.randint(100000, 999999)
        student_id: int = user_manager.random_id()
        if update_date is not None:
            student_id = update_date['id']
        print(f"\nID: {student_id}\nUsername: {random_username}\nFull name: {fullname}\nEmail: {email}\n"
              f"Gender: {gender}\nPhone number: {phone_number}\nAge: {age}\nPassword: {random_password}")
        print(f"\nusername: {random_username}\npassword: {random_password}")
        student_data = {f'{student_id}': {
            "id": student_id,
            "username": random_username,
            "full_name": fullname,
            "password": hashlib.sha256(str(random_password).encode('utf-8')).hexdigest(),
            "role": "student",
            "create_date": self.__created_data,
            "age": age,
            "gender": gender,
            "phone_number": phone_number,
            "email": email,
            "xp": 0,
            "is_login": False
        }}
        threading.Thread(target=user_manager.append_data, args=(student_data,)).start()
        if update_date is None:
            print("\nStudent added successfully.")
        email_subject = "Your username and password"
        body = f'Your id: {student_id}\nUsername: {random_username}\nPassword: {random_password}'
        threading.Thread(target=email_sender.only_send_email,
                         kwargs={'subject': email_subject, 'body': body, 'to_email': email}).start()
        print('\nInformation has been sent to the student\n')
        return True

    @log_decorator
    def update_student(self):
        for student in self.show_all_students():
            if student is None or student is False:
                print("Students not found")
                return False
            print(student)
        choose_student = int(input('\nChoose student id: '))
        result_get = user_manager.get_data(data_id=choose_student)
        if result_get is False or result_get['role'] != 'student':
            print("Student not found")
            return False
        print(f"\nID: {result_get['id']}\nUsername: {result_get['username']}\nFull name: {result_get['full_name']}\n"
              f"Email: {result_get['email']}\nGender: {result_get['gender']}\n"
              f"Phone number: {result_get['phone_number']}\nAge: {result_get['age']},\nXP: {result_get['xp']},\n"
              f"Created: {result_get['create_date']}")
        print("\nEnter new data\n")
        if self.add_student(update_date=result_get):
            print("Student update successfully.")
            return True
        print("Student update failed.")
        return False

    @log_decorator
    def delete_student(self):
        for student in self.show_all_students():
            if student is None and student is False:
                print("Student is not found")
                return False
            print(student)
        choose_student = int(input('\nChoose student id: '))
        result_get = user_manager.get_data(data_id=choose_student)
        if result_get is False or result_get['role'] != 'student':
            print("Student not found")
            return False
        threading.Thread(target=user_manager.delete_data, args=(result_get['id'],)).start()
        print("\nStudent deleted successfully.")
        return True
