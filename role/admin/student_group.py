import threading
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import group_manager, user_manager, payment_manager
from role.admin.group_menu import GroupMenu
from role.super_admin.student_menu import StudentMenu


class StudentGroup:
    def __init__(self):
        self.__student_menu = StudentMenu()
        self.__group_menu = GroupMenu()

    @log_decorator
    def add_student_to_group(self) -> bool:
        print("Choose group: ")
        for group in self.__group_menu.show_all_group():
            if group is False:
                print("Group not found")
                return False
            print(group)
        choose_group: int = int(input("\nEnter group id: "))
        print("\n Choose student: ")
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
        get_group: dict = group_manager.get_data(data_id=choose_group)
        if choose_student in get_group['students']:
            print("Student already in group")
            return False
        elif get_group['max_student'] == len(get_group['students']):
            print("The group is full")
            return False
        get_group['students'].append(get_student['id'])
        group_data = {f'{get_group["id"]}': get_group}
        threading.Thread(target=group_manager.append_data, args=(group_data,)).start()
        print("Student added to group")
        return True

    @log_decorator
    def search_student(self) -> bool or str:
        all_students: dict = user_manager.read()
        count = 1
        key_word = input("Search: ").strip().lower()
        for student in all_students.values():
            if student['role'] == 'student':
                if key_word in student['full_name'].lower() or key_word in student['username']:
                    yield (f"{count}. ID: {student['id']}, Fullname: {student['full_name']}, "
                           f" Username: {student['username']}, Age: {student['age']}, Email: {student['email']}, "
                           f"Gender: {student['gender']}, Role: {student['role']}, XP: {student['xp']} "
                           f"Phone number: {student['phone_number']},  Created: {student['create_date']}")
                    count += 1
        if count == 1:
            print("No students found.")
            return False

    @log_decorator
    def student_payment(self) -> bool:
        for student in self.__student_menu.show_all_students():
            if student is False or student is None:
                print("Student not found")
                return False
            print(student)
        choose_student: int = int(input("\nEnter student id: "))
        get_student: dict = user_manager.get_data(data_id=choose_student)
        if get_student is False or get_student is None:
            print("Student not found")
            return False
        elif get_student['role'] != 'student':
            print("Student not found")
            return False
        amount: int = int(input("Enter amount(uzs): "))
        data_id: int = payment_manager.random_id()
        data = {f'{data_id}': {
            'id': data_id,
            'amount': amount,
            'student_id': get_student['id'],
            'create_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        }}
        threading.Thread(target=payment_manager.append_data, args=(data,)).start()
        print("Payment submit")
        return True

    @log_decorator
    def show_all_payment(self):
        pass
