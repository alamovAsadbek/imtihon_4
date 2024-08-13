import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class GroupMenu:
    def __init__(self):
        self.__created_data = datetime.datetime.now().strftime("%y%m%d%H%M%S").__str__()

    @log_decorator
    def show_all_teacher(self):
        all_teacher: dict = user_manager.read()
        count = 1
        for teacher in all_teacher.values():
            if teacher['role'] == 'teacher':
                yield f"{count}. ID: {teacher['id']}, Fullname: {teacher['full_name']}, Username: {teacher['username']}, "
                f"Age: {teacher['age']}, Gender: {teacher['gender']}, Role: {teacher['role']}, "
                f"Created: {teacher['create_date']}"
                count += 1
        if count == 1:
            return False

    @log_decorator
    def create_group(self):
        group_name = input("Enter a group name: ").strip()
        for teacher in self.show_all_teacher():
            if teacher is False:
                print("Teacher not found")
                return False
            print(teacher)
        choose_teacher: int = int(input("Enter teacher id: "))
        get_teacher: dict = user_manager.get_data(data_id=choose_teacher)
        if get_teacher is False:
            print("Teacher not found")
            return False
