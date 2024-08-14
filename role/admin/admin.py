import datetime

from main_files.decorator_func import log_decorator
from role.admin.group_menu import GroupMenu
from role.admin.student_group import StudentGroup
from role.super_admin.student_menu import StudentMenu


class Admin:

    def __init__(self):
        self.__created_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
        self.__group_menu = GroupMenu()
        self.__student_menu = StudentMenu()
        self.__student_group = StudentGroup()

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
        for group in self.__group_menu.show_all_group():
            print(group)
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
        self.__student_group.add_student_to_group()
        return True

    # /add student to group

    # search student
    @log_decorator
    def search_student(self) -> bool:
        for data in self.__student_group.search_student():
            if data is False or data is None:
                return False
            print(data)
        return True

    # /search student

    # payment
    @log_decorator
    def payment_student(self) -> bool:
        self.__student_group.student_payment()
        return True

    @log_decorator
    def show_all_payment(self):
        for payment in self.__student_group.show_all_payment():
            if payment is False or payment is None:
                print("Payment not found")
                return False
            print(payment)
        return True

    @log_decorator
    def withdraw_payment_group(self):
        self.__student_group.withdraw_payment_group()
        return True

    @log_decorator
    def withdraw_payment_student(self):
        self.__student_group.withdraw_payment_student()
        return True
    # /payment
