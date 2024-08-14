import threading

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager


class Student:
    def __init__(self):
        self.__active_student = user_manager.get_active_user()
        self.__admin_email = 'alamovasad@gmail.com'

    @log_decorator
    def show_my_groups(self) -> bool:
        all_group: dict = group_manager.read()
        count = 1
        for group in all_group:
            if self.__active_student['id'] in group['students']:
                print(
                    f"{count}. Group ID: {group['id']}, Group name: {group['name']}, Max student: "
                    f"{group['max_student']}, Start time: {group['start_time']}, End time: {group['end_time']}")
                count += 1
        if count == 1:
            print("Your group is not found")
            return False
        return True

    @log_decorator
    def student_profile(self) -> bool:
        print(f"\nID: {self.__active_student['id']}\nUsername: {self.__active_student['username']}\n"
              f"Fullname: {self.__active_student['full_name']}\nAge: {self.__active_student['age']}\n"
              f"Gender: {self.__active_student['gender']}\nPhone number: {self.__active_student['phone_number']}\n"
              f"Email: {self.__active_student['email']}\nXP: {self.__active_student['xp']}\n"
              f"Registered: {self.__active_student['create_date']}")

        while True:
            print('\n1. Back \t 2. Update profile\n')
            user_input: int = int(input("Choose: "))
            if user_input < 1 or user_input > 2:
                print("Invalid input")
                continue
            elif user_input == 1:
                return True
            elif user_input == 2:
                self.update_profile()
                return True
            else:
                print("Error")
                return False
        return True

    @log_decorator
    def update_profile(self):
        print("\nEnter new data\n")
        fullname: str = input("Fullname: ").strip()
        while True:
            email: str = input('Email: ').strip()
            if not user_manager.is_valid_email_format(email=email):
                print("Email validation failed, please try again.")
                print("Example: email@gmail.com")
                continue
            elif email == self.__active_student['email']:
                pass
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
            if phone_number == self.__active_student['phone_number']:
                pass
            elif user_manager.check_data_by_key(key='phone_number', value=phone_number):
                print("This phone number is already in use.")
                continue
            break
        student_data = {
            f'{self.__active_student["id"]}': {
                "id": self.__active_student["id"],
                "username": self.__active_student['username'],
                "full_name": fullname,
                "password": self.__active_student['password'],
                "role": "student",
                "create_date": self.__active_student['create_date'],
                "age": age,
                "gender": gender,
                "phone_number": phone_number,
                "email": email,
                "xp": self.__active_student['xp'],
                "is_login": False
            }
        }
        threading.Thread(target=user_manager.append_data, args=(student_data,)).start()
        print("Your profile updated")
        return True
