import contextlib
import json
import os
import random
import threading

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
                json.dump({}, file, indent=4)
                return {}

    @log_decorator
    def write(self, data) -> bool:
        with self.open_json(mode="w") as file:
            json.dump(data, file, indent=4)
            return True

    @log_decorator
    def append_data(self, data) -> bool:
        try:
            all_data: dict = self.read()
            all_data.update(data)
            self.write(all_data)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def get_active_user(self) -> dict or bool:
        all_users: list = self.read()
        try:
            for key, value in all_users:
                if value['is_login']:
                    return value
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def get_data(self, data_id) -> dict or bool:
        all_users: dict = self.read()
        try:
            if data_id.__str__() in all_users.keys():
                return all_users[data_id.__str__()]
            return False
        except KeyError:
            return False

    @log_decorator
    def delete_data(self, data_id: int) -> bool:
        all_data: dict = self.read()
        for index, data in enumerate(all_data.keys()):
            if data_id.__str__() == data:
                del all_data[data]
                threading.Thread(target=self.write, args=(all_data,)).start()
                return True
        return False

    @log_decorator
    def check_data_by_key(self, key: str, value: str) -> bool:
        all_users: dict = self.read()
        for user in all_users.values():
            if user[key] == data:
                return True
        return False

    @log_decorator
    def random_id(self):
        try:
            all_data: dict = self.read()
            while True:
                random_number: int = random.randint(1, 99999)
                if random_number.__str__() in all_data.keys():
                    continue
                return random_number
        except Exception as e:
            print(f'Error: {e}')
            return False


user_manager = JsonManager(file_name='data/users.json')
