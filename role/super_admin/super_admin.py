import datetime

from main_files.decorator_func import log_decorator
from role.super_admin.admin_menu import AdminMenu
from role.super_admin.student_menu import StudentMenu


class SuperAdmin:
    def __init__(self):
        self.__create_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        self.__admin_username = 'admin'
        self.__admin_password = 'admin'
        self.__admin_menu = AdminMenu()
        self.__student_menu = StudentMenu()

    # admin menu

    # show all admins
    @log_decorator
    def show_all_admins(self) -> bool:
        self.__admin_menu.show_all_admins()
        return True

    # add new admin
    @log_decorator
    def add_new_admin(self, out_data: dict = None) -> bool:
        self.__admin_menu.add_new_admin(out_data)
        return True

    # update admin
    @log_decorator
    def update_admin(self) -> bool:
        self.__admin_menu.update_admin()
        return True

    # delete admin by admin id
    @log_decorator
    def delete_admin(self) -> bool:
        self.__admin_menu.delete_admin()
        return True

    # /admin menu

    # student
    @log_decorator
    def add_student(self) -> bool:
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
    def show_all_students(self):
        for student in self.__student_menu.show_all_students():
            if student is None or student is False:
                print("Student Not Found")
            print(student)
        return True
