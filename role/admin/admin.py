import datetime

from main_files.decorator_func import log_decorator
from role.admin.group_menu import GroupMenu


class Admin:
    def __init__(self):
        self.__created_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
        self.__group_menu = GroupMenu()

    # group
    @log_decorator
    def create_group(self) -> bool:
        self.__group_menu.create_group()
        return True

    @log_decorator
    def delete_group(self) -> bool:
        self.__group_menu.delete_group()
        return True
    # /group
