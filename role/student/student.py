from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager


class Student:
    def __init__(self):
        self.__active_student = user_manager.get_active_user()

    @log_decorator
    def show_my_groups(self):
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
