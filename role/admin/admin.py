import datetime

from main_files.decorator_func import log_decorator
from role.admin.group_menu import GroupMenu
from role.super_admin.student_menu import StudentMenu


class Admin:
    def __init__(self):
        self.__created_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
        self.__group_menu = GroupMenu()
        self.__student_menu = StudentMenu()

    # group
    @log_decorator
    def create_group(self) -> bool:
        self.__group_menu.create_group()
        return True

    @log_decorator
    def delete_group(self) -> bool:
        self.__group_menu.delete_group()
        return True

    @log_decorator
    def show_all_groups(self) -> bool:
        self.__group_menu.show_all_group()
        return True

    # /group

    # student
    @log_decorator
    def create_student(self) -> bool:
        self.__student_menu.add_student()
        return True

    @log_decorator
    def update_student(self) -> bool:
        self.__student_menu.update_student()
        return True

    @log_decorator
    def delete_student(self) -> bool:
        self.__student_menu.delete_student()
        return True

    @log_decorator
    def show_all_student(self) -> bool:
        self.__student_menu.show_all_students()
        return True

    # / student

    # add student to group
    @log_decorator
    def add_student_to_group(self) -> bool:
        pass
    # /add student to group
