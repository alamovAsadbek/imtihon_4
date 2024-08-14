import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager


class Teacher:
    def __init__(self):
        self.__create_date = datetime.datetime.now().strftime('%d.%m.%Y').__str__()
        self.__active_teacher = user_manager.get_active_user()

    @log_decorator
    def my_groups(self) -> bool:
        all_groups: dict = group_manager.read()
        count = 1
        for group in all_groups.values():
            if group['teacher'] == self.__active_teacher:
                print(f'{count}. Group name: {group["name"]}, Max students: {group["max_students"]}, '
                      f'Start time: {group["start_time"]}, End time: {group["end_time"]}, '
                      f'Current students: {len(group["students"])}, Status: {group["status"]}, '
                      f'Created: {group["create_date"]}, ')
                count += 1
        if count == 1:
            print("Your group is not found")
            return False
        return True
