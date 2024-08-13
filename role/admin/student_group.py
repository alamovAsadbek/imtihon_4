from main_files.decorator_func import log_decorator
from main_files.json_manager import group_manager
from role.admin.group_menu import GroupMenu
from role.super_admin.student_menu import StudentMenu


class StudentGroup:
    def __init__(self):
        self.__student_menu = StudentMenu()
        self.__group_menu = GroupMenu()

    @log_decorator
    def add_student_to_group(self):
        for group in self.__group_menu.show_all_group():
            if group is False:
                print("Group not found")
                return False
            print(group)
        choose_group: int = int(input("\nEnter group id: "))
        if not group_manager.check_data_by_key(key='id', value=choose_group):
            print("Group not found")
            return False
        for student in self.__student_menu.show_all_students():
            if student is False:
                print("Student not found")
                return False
            print(student)
