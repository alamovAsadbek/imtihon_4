import random
import re

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class StudentMenu:
    @log_decorator
    def add_student(self):
        fullname: str = input('Full name: ').strip()
        while len(fullname) < 3:
            print('Full name must be at least 3 characters.')
            fullname = input('Full name: ').strip()
        while True:
            random_number: int = random.randint(1, 10000)
            name: str = fullname.split()[0]
            name = re.sub('[^A-Za-z]+', '', name)
            random_username: str = f'student_{name.lower()}_{random_number}'
            if user_manager.check_data_by_key(key='username', value=random_username):
                continue
            break
        email: str = input('Email: ').strip()
        while not user_manager.is_valid_email_format(email):
            print("Email validation failed, please try again.")
            print("Example: email@gmail.com")
            email: str = input('Email: ').strip()
        while user_manager.check_data_by_key(key='email', value=email):
            print("This email is already in use.")
            email: str = input('Email: ').strip()
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
        phone_number: str = input('Phone number (+998): ').strip()
        while user_manager.check_data_by_key(key='phone_number', value=phone_number):
            print("This phone number is already in use.")
            phone_number: str = input('Phone number (+998): ').strip()
        random_password: int = random.randint(100000, 999999)
        student_id = user_manager.random_id()
        print(f"\nID: {student_id}\nUsername: {random_username}\nFull name: {fullname}\nEmail: {email}\n"
              f"Gender: {gender}\nPhone number: {phone_number}\nAge: {age}\nPassword: {random_password}")
        print(f"\nusername: {random_username}\npassword: {random_password}")
        return True
