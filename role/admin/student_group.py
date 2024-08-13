import threading

from main_files.decorator_func import log_decorator
from main_files.json_manager import group_manager, user_manager
from role.admin.group_menu import GroupMenu
from role.super_admin.student_menu import StudentMenu


class StudentGroup:
    def __init__(self):
        self.__student_menu = StudentMenu()
        self.__group_menu = GroupMenu()

    @log_decorator
    def add_student_to_group(self) -> bool:
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
        choose_student: int = int(input("\nEnter student id: "))
        get_student: dict = user_manager.get_data(data_id=choose_student)
        if get_student is None or get_student is False or get_student['role'] != 'student':
            print("Student not found")
            return False
        get_group: dict = group_manager.get_data(group_id=choose_group)
        get_group['students'].append(get_student['id'])
        group_data = {f'{get_group["id"]}': get_group}
        threading.Thread(target=group_manager.append_data, args=(group_data,)).start()
        print("Student added to group")
        return True
