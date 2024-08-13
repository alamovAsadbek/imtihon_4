import re
import threading
from calendar import monthrange
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, group_manager


class GroupMenu:
    def __init__(self):
        self.__create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()

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
    def show_all_group(self):
        all_group: dict = group_manager.read()
        count = 1
        for group in all_group.values():
            teacher = user_manager.get_data(data_id=group['teacher'])
            yield (f"{count}. ID: {group['id']}, Name: {group['name']}, Max student: {group['max_student']}, "
                   f"Start time: {group['start_time']}, End time: {group['end_time']}, "
                   f"Teacher name: {teacher['full_name']}, Current students: {len(group['students'])}, "
                   f"Status: {group['status']}")
            count += 1
        if count == 1:
            return False

    @log_decorator
    def add_months(self, date_string, months_to_add):
        try:
            date = datetime.strptime(date_string, "%d.%m.%Y")
            year = date.year
            month = date.month
            day = date.day
            new_month = month + months_to_add
            new_year = year + new_month // 12
            new_month = new_month % 12 if new_month % 12 != 0 else 12
            new_year = new_year if new_month != 12 else new_year - 1
            last_day_of_new_month = monthrange(new_year, new_month)[1]
            new_day = min(day, last_day_of_new_month)
            new_date = datetime(new_year, new_month, new_day).date()
            return new_date.strftime("%d.%m.%Y")
        except ValueError:
            return False

    @log_decorator
    def create_group(self):
        group_name = input("Enter a group name: ").strip()
        while True:
            if group_manager.check_data_by_key(key='name', value=group_name):
                print(f"Group {group_name} already exists")
                continue
            break
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
        max_student: int = int(input("Enter maximum student number: "))
        while max_student < 10:
            print("Max student number is less than 10")
            max_student: int = int(input("Enter maximum student number: "))
        start_time: str = input("Enter start time(dd.mm.yyyy): ").strip()
        while True:
            pattern = r"^\d{2}\.\d{2}\.\d{4}$"
            check_date = bool(re.match(pattern, start_time))
            today = datetime.now().strftime("%d%m%y")
            if not check_date or today < start_time:
                print("Start date is invalid")
                start_time: str = input("Enter start time(dd.mm.yyyy): ").strip()
                continue
            break
        course_duration: int = int(input("Enter course duration (month): "))
        end_data = self.add_months(start_time, course_duration)
        if end_data is False:
            print("Something went wrong")
            return False
        group_id = group_manager.random_id()
        group_data = {f'{group_id}': {
            'id': group_id,
            'name': group_name,
            'max_student': max_student,
            'start_time': start_time,
            'end_time': end_data,
            'teacher': get_teacher['id'],
            'status': 'not_started',
            'students': [],
            'create_date': self.__create_date
        }}
        threading.Thread(target=group_manager.append_data, args=(group_data,)).start()
        print(f"Group {group_name} created successfully")
        return True

    @log_decorator
    def delete_group(self):
        for group in self.show_all_group():
            if group is False:
                print("Group not found")
                return False
            print(group)
        group_choose: int = int(input("Enter group id: "))
