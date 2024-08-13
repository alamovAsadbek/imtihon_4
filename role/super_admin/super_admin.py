import datetime

from main_files.decorator_func import log_decorator
from role.super_admin.admin import Admin


class SuperAdmin:
    def __init__(self):
        self.__create_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        self.__admin_username = 'admin'
        self.__admin_password = 'admin'
        self.admin_menu = Admin()

    # admin menu

    # show all admins
    @log_decorator
    def show_all_admins(self) -> bool:
        self.admin_menu.show_all_admins()
        return True

    # add new admin
    @log_decorator
    def add_new_admin(self, out_data: dict = None) -> bool:
        self.admin_menu.add_new_admin(out_data)
        return True

    # update admin
    @log_decorator
    def update_admin(self) -> bool:
        self.admin_menu.update_admin()
        return True

    # delete admin by admin id
    @log_decorator
    def delete_admin(self) -> bool:
        self.admin_menu.delete_admin()
        return True
    # /admin menu
