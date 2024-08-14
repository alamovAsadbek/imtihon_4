import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager
from role.admin.group_menu import GroupMenu


class Teacher:
    def __init__(self):
        self.__create_date = datetime.datetime.now().strftime('%d.%m.%Y').__str__()
        self.__active_teacher = user_manager.get_active_user()
        self.__group_menu = GroupMenu()

    @log_decorator
    def my_groups(self) -> bool:
        all_groups: dict = group_manager.read()
        count = 1
        for group in all_groups.values():
            if group['teacher'] == self.__active_teacher['id']:
                print(f'{count}.ID: {group["id"]}, Group name: {group["name"]}, Max students: {group["max_student"]}, '
                      f'Start time: {group["start_time"]}, End time: {group["end_time"]}, '
                      f'Current students: {len(group["students"])}, Status: {group["status"]}, '
                      f'Created: {group["create_date"]}, ')
                count += 1
        if count == 1:
            print("Your group is not found")
            return False
        return True

    @log_decorator
    def show_student_to_group(self) -> bool:
        count = 1
        if not self.my_groups():
            return False
        choose_group: int = int(input("Enter group id: "))
        get_group: dict = group_manager.get_data(data_id=choose_group)
        if get_group is None or get_group is False:
            print("Group not found")
            return False
        elif get_group['teacher'] != self.__active_teacher['id']:
            print("Group not found")
            return False
        print(f"Group ID: {get_group['id']}, Group name: {get_group['name']}, Max student: {get_group['max_student']},"
              f" Start time: {get_group['start_time']}, End time: {get_group['end_time']}")
        print("\nGroup students: ")
        for student in get_group['students']:
            get_student: dict = user_manager.get_data(data_id=student)
            if get_student is None or get_student is False:
                continue
            print(f"{count}. ID: {student}, Fullname: {get_student['full_name']}, Username: {get_student['username']}, "
                  f"XP: {get_student['xp']}")
            count += 1
        if count == 1:
            print("Group's students not found")
            return False
        return True
