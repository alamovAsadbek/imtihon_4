import contextlib
import json
import os
import random

from main_files.decorator_func import log_decorator

if not os.path.exists('data'):
    os.makedirs('data')


class JsonManager:
    def __init__(self, file_name):
        self.file_name: str = file_name

    @log_decorator
    @contextlib.contextmanager
    def open_json(self, mode: str):
        file = open(self.file_name, mode)
        yield file
        file.close()

    @log_decorator
    def read(self) -> dict or bool:
        try:
            with self.open_json(mode='r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            with self.open_json(mode='w') as file:
                json.dump([], file, indent=4)
                return []

    @log_decorator
    def write(self, data) -> bool:
        with self.open_json(mode="w") as file:
            json.dump(data, file, indent=4)
            return True

    @log_decorator
    def check_username(self, username) -> bool:
        all_users: list = self.read()
        try:
            for user in all_users:
                if user['username'] == username:
                    return True
            return False
        except KeyError:
            return False

    @log_decorator
    def append_data(self, data) -> bool:
        try:
            all_data: list = self.read()
            all_data.append(data)
            self.write(all_data)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def get_active_user(self) -> dict or bool:
        all_users: list = self.read()
        try:
            for user in all_users:
                if user['is_login']:
                    return user
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def get_data(self, data_id) -> dict or bool:
        all_users: list = self.read()
        try:
            for data in all_users:
                if data['id'] == data_id:
                    return data
            return False
        except KeyError:
            return False

    @log_decorator
    def random_id(self):
        try:
            all_data: list = self.read()
            while True:
                random_number: int = random.randint(1, 9999)
                for data in all_data:
                    if data['id'] == random_number:
                        break
                return random_number
        except Exception as e:
            print(f'Error: {e}')
            return False


user_manager = JsonManager(file_name='data/users.json')
