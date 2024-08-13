import hashlib
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class Auth:
    def __init__(self):
        self.create_data = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        self.__admin_username = "admin"
        self.__admin_password = "admin"

    @log_decorator
    def login(self) -> dict:
        all_users: dict = user_manager.read()
        username: str = input("Username: ").strip().lower()
        password: str = hashlib.sha256(input('Enter password: ').strip().encode('utf-8')).hexdigest()
        if username == self.__admin_username and password == hashlib.sha256(
                self.__admin_password.encode('utf-8')).hexdigest():
            return {'is_login': True, 'role': 'super_admin'}
        if not user_manager.check_data_by_key(key='username', value=username):
            print('Username not found')
            return {'is_login': False, 'role': "admin"}
        for user in all_users.values():
            if user['username'] == username and user['password'] == password:
                user['is_login'] = True
                if user_manager.write(data=all_users):
                    print('Login successful')
                    return {'is_login': True, 'role': user['role']}
        print('Login failed')
        return {'is_login': False, 'role': 'admin'}

    @log_decorator
    def logout(self) -> bool:
        try:
            all_users: dict = user_manager.read()
            for user in all_users.values():
                user['is_login'] = False
            user_manager.write(all_users)
            return True
        except ValueError:
            return True
