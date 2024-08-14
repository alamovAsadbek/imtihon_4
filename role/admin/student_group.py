import threading
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.email_sender import EmailSender
from main_files.json_manager import group_manager, user_manager, payment_manager
from role.admin.group_menu import GroupMenu
from role.super_admin.student_menu import StudentMenu


class StudentGroup:
    def __init__(self):
        self.__student_menu = StudentMenu()
        self.__group_menu = GroupMenu()
        self.__email_sender = EmailSender()
        self.__created_data = datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()

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
        all_payments: dict = payment_manager.read()
        count = 1
        for payment in all_payments.values():
            get_student = user_manager.get_data(data_id=payment['student_id'])
            status = 'filled'
            if payment['amount'] < 1:
                status = 'withdraw'
                payment['amount'] *= -1
            yield (f"{count}. Payment ID: {payment['id']}, Student fullname: {get_student['full_name']}, "
                   f"Student ID: {get_student['id']}, Amount: {payment['amount']} UZS, Status: {status} "
                   f"Time: {payment['create_date']}")
            count += 1

    @log_decorator
    def count_balance(self, user_id: int):
        all_balance: dict = payment_manager.read()
        summ = 0
        for payment in all_balance.values():
            if payment['student_id'] == user_id:
                summ += payment['amount']
        return summ

    @log_decorator
    def withdraw_payment_group(self):
        email_subject = "Payment"
        email_body: str = ''
        for group in self.__group_menu.show_all_group():
            if group is False or group is None:
                print("Groups not found")
                return False
            print(group)
        choose_group: int = int(input("Enter group id: "))
        amount: int = int(input("Amount(uzs): "))
        get_data: dict = group_manager.get_data(data_id=choose_group)
        if get_data is False or get_data is None:
            print("Group not found")
            return False
        for pay_data in get_data['students']:
            student_balance = self.count_balance(user_id=pay_data)
            if student_balance >= amount:
                data_id = payment_manager.random_id()
                data = {f"{data_id}": {
                    "id": data_id,
                    "amount": -amount,
                    "student_id": pay_data,
                    "create_date": self.__created_data
                }}
                threading.Thread(target=payment_manager.append_data, args=(data,)).start()
                email_body = f"{amount} uzs have been withdrawn from your account"
            else:
                email_body = 'You do not have enough money for the course, please top up your account'
            threading.Thread(target=self.__email_sender.send_email, args=('all', email_subject, email_body)).start()
            print("Finished")
            return True

    @log_decorator
    def withdraw_payment_student(self):
        for student in self.__student_menu.show_all_students():
            if student is False or student is None:
                print("Student not found")
                return False
            print(student)
        student_id: int = int(input("Enter student id: ").strip())
        get_student: dict = user_manager.get_data(data_id=student_id)
        if get_student is False or get_student is None:
            print("Student not found")
            return False
        elif get_student['role'] != 'student':
            print("Student not found")
            return False
        student_balance = self.count_balance(student_id)
        print(f"Student balance: {student_balance}")
        amount: int = int(input("Amount: "))
        if amount > student_balance:
            print("Funds are insufficient")
            return False
        data_id = payment_manager.random_id()
        data = {f"{data_id}": {
            "id": data_id,
            "amount": -amount,
            "student_id": get_student['id'],
            "create_date": self.__created_data
        }}
        threading.Thread(target=payment_manager.append_data, args=(data,)).start()
        email_subject = "Payment"
        email_body = f"{amount} uzs have been withdrawn from your account"
        threading.Thread(target=self.__email_sender.send_email, args=('all', email_subject, email_body)).start()
        print("Finished")
        return True
