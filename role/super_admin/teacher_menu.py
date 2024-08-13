import hashlib
import threading
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class TeacherMenu:
    def __init__(self):
        self.__create_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        self.__admin_username = 'admin'
        self.__admin_password = 'admin'

    # teacher menu

    # show all teachers
    @log_decorator
    def show_all_teacher(self) -> bool:
        all_teacher: dict = user_manager.read()
        count = 1
        if len(all_teacher) == 0:
            print('No teachers found.')
            return False
        for teacher in all_teacher.values():
            if teacher['teacher'] == 'teacher':
                print(
                    f"{count}. ID: {teacher['id']}, Fullname: {teacher['full_name']}, Username: {teacher['username']}, "
                    f"Age: {teacher['age']}, Gender: {teacher['gender']}, Role: {teacher['role']}, "
                    f"Created: {teacher['create_date']}")
                count += 1
        if count == 1:
            print("Teacher not found.")
            return False
        return True

    # add new teacher
    @log_decorator
    def add_new_teacher(self, out_data: dict = None) -> bool:
        full_name = input('Full name: ').strip()
        username = input('Username: ').strip()
        age: int = int(input('Age: ').strip())
        while True:
            if out_data is not None and out_data['username'] == username:
                break
            if user_manager.check_data_by_key(key='username', value=username) or username == self.__admin_username:
                print('Username is taken. Please try again.')
                username = input('Username: ').strip()
                continue
            break
        gender = 'male'
        while True:
            print("Choose gender:")
            print(f'1. Male \t 2. Female')
            user_choice: int = int(input('Enter your choice: ').strip())
            if user_choice < 1 or user_choice > 2:
                print('Invalid choice. Please try again.')
                continue
            elif user_choice == 1:
                gender = 'male'
                break
            elif user_choice == 2:
                gender = 'female'
                break
            else:
                print('Invalid choice. Please try again.')
        while True:
            password = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
            confirm_password = hashlib.sha256(input('Confirm password: ').strip().encode('utf-8')).hexdigest()
            if password == confirm_password:
                break
            print('Passwords do not match. Please try again.')
        data_id = user_manager.random_id()
        if out_data is not None:
            data_id = out_data['id']
            self.__create_data = out_data['create_date']
        data = {f'{data_id}': {
            'id': data_id,
            'username': username,
            'full_name': full_name,
            'password': password,
            'role': 'teacher',
            'create_date': self.__create_data,
            "age": age,
            "gender": gender,
            "phone_number": False,
            "email": False,
            "xp": 0,
            'is_login': False
        }}
        threading.Thread(target=user_manager.append_data, args=(data,)).start()
        if out_data is None:
            print('Teacher added successfully.')
        return True

    # update teacher
    @log_decorator
    def update_teacher(self) -> bool:
        if not self.show_all_teacher():
            return False
        choose_teacher = int(input('\nEnter teacher id:  ').strip())
        get_teacher = user_manager.get_data(data_id=choose_teacher)
        if get_teacher is False:
            print('No teacher found.')
            return False
        print(f'\nID: {get_teacher["id"]}\nFullname: {get_teacher["full_name"]}\n'
              f'Username: {get_teacher["username"]}\n')
        if self.add_new_teacher(out_data=get_teacher):
            print('Teacher successfully updated.')
            return True
        print("Something went wrong. Please try again.")
        return False

    # delete teacher by admin id
    @log_decorator
    def delete_taecher(self) -> bool:
        if not self.show_all_teacher():
            return False
        teacher_id = int(input('\nEnter teacher id: ').strip())
        if user_manager.delete_data(data_id=teacher_id):
            print('Teacher successfully deleted.')
            return True
        print("Something went wrong. Please try again.")
        return False
    # /taecher menu
