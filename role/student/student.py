from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager


class Student:
    def __init__(self):
        self.__active_student = user_manager.get_active_user()

    @log_decorator
    def show_my_groups(self) -> bool:
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

    @log_decorator
    def student_profile(self):
        print(f"ID: {self.__active_student['id']}\nUsername: {self.__active_student['username']}\n"
              f"Fullname: {self.__active_student['full_name']}\nAge: {self.__active_student['age']}\n"
              f"Gender: {self.__active_student['gender']}\nPhone number: {self.__active_student['phone_number']}\n"
              f"Email: {self.__active_student['email']}\nXP: {self.__active_student['xp']}\n"
              f"Registered: {self.__active_student['create_date']}")

        while True:
            print('1. Back \t 2. Update profile')
            user_input: int = int(input("Choose: "))
            if user_input < 1 or user_input > 2:
                print("Invalid input")
                continue

    @log_decorator
    def update_profile(self):
        pass
