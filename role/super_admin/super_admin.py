import datetime
import hashlib
import threading

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class SuperAdmin:
    def __init__(self):
        self.__create_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        self.__admin_username = 'admin'
        self.__admin_password = 'admin'

    # admin
    @log_decorator
    def show_all_admins(self) -> bool:
        all_admins: dict = user_manager.read()
        count = 1
        if len(all_admins) == 0:
            print('No admins found.')
            return False
        for admin in all_admins.values():
            if admin['role'] == 'admin':
                print(f"{count}. ID: {admin['id']} Fullname: {admin['full_name']}, Username: {admin['username']}, "
                      f"Role: {admin['role']}, Created: {admin['create_date']}")
                count += 1
        if count == 1:
            print("Admin not found.")
            return False
        return True

    @log_decorator
    def add_new_admin(self, data: dict = None) -> bool:
        full_name = input('Full name: ').strip()
        username = input('Username: ').strip()
        while True:
            if data is not None and data['username'] == username:
                break
            if user_manager.check_username(username=username) or username == self.__admin_username:
                print('Username is taken. Please try again.')
                username = input('Username: ').strip()
        while True:
            password = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
            confirm_password = hashlib.sha256(input('Confirm password: ').strip().encode('utf-8')).hexdigest()
            if password == confirm_password:
                break
            print('Passwords do not match. Please try again.')
        data_id = user_manager.random_id()
        if data is not None:
            data_id = data['id']
            self.__create_data = data['create_date']
        data = {f'{data_id}': {
            'id': data_id,
            'username': username,
            'full_name': full_name,
            'password': password,
            'role': 'admin',
            'create_date': self.__create_data,
            'is_login': False
        }}
        threading.Thread(target=user_manager.append_data, args=(data,)).start()
        return True

    @log_decorator
    def update_admin(self) -> bool:
        if not self.show_all_admins():
            return False
        choose_admin = int(input('\nEnter admin id:  ').strip())
        get_admin = user_manager.get_data(data_id=choose_admin)
        if get_admin is False:
            print('No admin found.')
            return False
        print(f'\nID: {get_admin["id"]}\nFullname: {get_admin["full_name"]}\n'
              f'Username: {get_admin["username"]}\n')
        if self.add_new_admin(data=get_admin):
            print('Admin successfully updated.')
            return True
        print("Something went wrong. Please try again.")
        return False

    @log_decorator
    def delete_admin(self) -> bool:
        if not self.show_all_admins():
            return False
        admin_id = int(input('\nEnter admin id: ').strip())
        get_admin = user_manager.get_data(data_id=admin_id)
        if get_admin is False:
            print('No admin found.')
            return False
