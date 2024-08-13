import random

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class StudentMenu:
    @log_decorator
    def add_student(self):
        fullname: str = input('Full name: ').strip()
        while True:
            random_number: int = random.randint(1, 10000)
            random_username: str = f'student_{fullname.lower()}_{random_number}'
            if user_manager.check_data_by_key(key='username', value=random_username):
                continue
            print(f"Random username: {random_username}")
        while True:
            email: str = input('Email: ').strip()
            if user_manager.check_data_by_key(key='email', value=email):
                print(f"Email already registered")
                continue
            break
        print(email)
        return True
