from main_files.auth import Auth
from main_files.decorator_func import log_decorator
from role.admin.admin import Admin
from role.super_admin.super_admin import SuperAdmin
from role.teacher.teacher import Teacher


# This function is auth menu
@log_decorator
def show_auth():
    text = '''
1. Login
2. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            result_login = auth.login()
            if not result_login['is_login']:
                show_auth()
            elif result_login['role'] == "super_admin":
                show_super_admin_menu()
            elif result_login['role'] == "admin":
                show_admin_menu()
            elif result_login['role'] == "teacher":
                show_teacher_menu()
            elif result_login['role'] == "student":
                show_student_menu()
            else:
                print("Something went wrong")
                show_auth()
        elif user_input == 2:
            print("Good bye!")
            return True
        else:
            print('Wrong input')
            show_auth()
    except ValueError:
        print("Invalid input")
        show_auth()
    except Exception as e:
        print(f'Error: {e}')
        show_auth()


# this function for super admin
@log_decorator
def show_super_admin_menu():
    text = '''
1. Admin
2. Student 
3. Teacher
4. Send message
5. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Admin\n')
            super_admin_admin_menu()
        elif user_input == 2:
            print('\nHome -> Student\n')
            super_admin_student_menu()
        elif user_input == 3:
            print('\nHome -> Teacher\n')
            super_admin_teacher_menu()
        elif user_input == 4:
            print('\nHome -> Message\n')
            super_admin_email_menu()
        elif user_input == 5:
            print("Logout successful")
            auth.logout()
            show_auth()
        else:
            print('Wrong input')
            show_super_admin_menu()
    except ValueError:
        print("Invalid input")
        show_super_admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_super_admin_menu()


@log_decorator
def super_admin_admin_menu():
    text = '''
1. Add Admin
2. Update Admin
3. Delete Admin
4. Show all Admins
5. Back
    '''
    print(text)
    try:
        super_admin = SuperAdmin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Admin -> Add admin\n')
            super_admin.add_new_admin()
            super_admin_admin_menu()
        elif user_input == 2:
            print('\nHome -> Admin -> Update admin\n')
            super_admin.update_admin()
            super_admin_admin_menu()
        elif user_input == 3:
            print('\nHome -> Admin -> Delete admin\n')
            super_admin.delete_admin()
            super_admin_admin_menu()
        elif user_input == 4:
            print('\nHome -> Admin -> Show all admins\n')
            super_admin.show_all_admins()
            super_admin_admin_menu()
        elif user_input == 5:
            show_super_admin_menu()
        else:
            print('Wrong input')
            super_admin_admin_menu()
    except ValueError:
        print("Invalid input")
        super_admin_admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        super_admin_admin_menu()


@log_decorator
def super_admin_teacher_menu():
    text = '''
1. Add new teacher
2. Update teacher
3. Delete teacher
4. Show all teachers
5. Back
    '''
    print(text)
    try:
        super_admin = SuperAdmin()
        choose_teacher = int(input('Choose menu: '))
        if choose_teacher == 1:
            print('\nHome -> Teacher -> Create\n')
            super_admin.create_teacher()
            super_admin_teacher_menu()
        elif choose_teacher == 2:
            print('\nHome -> Teacher -> Update\n')
            super_admin.update_teacher()
            super_admin_teacher_menu()
        elif choose_teacher == 3:
            print('\nHome -> Teacher -> Delete\n')
            super_admin.delete_teacher()
            super_admin_teacher_menu()
        elif choose_teacher == 4:
            print('\nHome -> Teacher -> Show all teachers\n')
            super_admin.show_all_teachers()
            super_admin_teacher_menu()
        elif choose_teacher == 5:
            show_super_admin_menu()
    except ValueError:
        print("Invalid input")
        super_admin_teacher_menu()
    except Exception as e:
        print(f'Error: {e}')
        super_admin_teacher_menu()


@log_decorator
def super_admin_email_menu():
    text = '''
1. All student
2. Only male
3. Only female
4. Back
    '''
    print(text)
    try:
        super_admin = SuperAdmin()
        choice = int(input('Choose menu: '))
        if choice == 1:
            print('\nHome -> Message -> All student\n')
            super_admin.send_all()
            super_admin_email_menu()
        elif choice == 2:
            print('\nHome -> Message -> Only male\n')
            super_admin.send_male()
            super_admin_email_menu()
        elif choice == 3:
            print('\nHome -> Message -> Only female\n')
            super_admin.send_female()
            super_admin_email_menu()
        elif choice == 4:
            show_super_admin_menu()
        else:
            print('Wrong input')
            super_admin_email_menu()
    except ValueError:
        print("Invalid input")
        super_admin_email_menu()
    except Exception as e:
        print(f'Error: {e}')
        super_admin_email_menu()


# student section belonging to super admin
@log_decorator
def super_admin_student_menu():
    text = '''
1. Create student
2. Update student
3. Delete student
4. Show all students
5. Back
    '''
    print(text)
    try:
        super_admin = SuperAdmin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Student -> Create student\n')
            super_admin.add_student()
            super_admin_student_menu()
        elif user_input == 2:
            print('\nHome -> Student -> Update student\n')
            super_admin.update_student()
            super_admin_student_menu()
        elif user_input == 3:
            print('\nHome -> Student -> Delete student\n')
            super_admin.delete_student()
            super_admin_student_menu()
        elif user_input == 4:
            print('\nHome -> Student -> Show all students\n')
            super_admin.show_all_students()
            super_admin_student_menu()
        elif user_input == 5:
            show_super_admin_menu()
    except ValueError:
        print("Invalid input")
        super_admin_student_menu()
    except Exception as e:
        print(f'Error: {e}')
        super_admin_student_menu()


# This section is for regular admins
@log_decorator
def show_admin_menu():
    text = '''
1. Group
2. Student
3. Teacher
4. Add a student to a group
5. Search student
6. Payment
7. Logout
    '''
    print(text)
    try:
        admin = Admin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Group\n')
            admin_group_menu()
        elif user_input == 2:
            print('\nHome -> Student\n')
            admin_student_menu()
        elif user_input == 3:
            print('\nHome -> Teacher\n')
            admin_teacher_menu()
        elif user_input == 4:
            print('\nHome -> Add student to group\n')
            admin.add_student_to_group()
            show_admin_menu()
        elif user_input == 5:
            print('\nHome -> Search student\n')
            admin.search_student()
            show_admin_menu()
        elif user_input == 6:
            print('\nHome -> Payment\n')
            payment_menu()
        elif user_input == 7:
            print("Logout successful")
            auth.logout()
            show_auth()
        else:
            print('Wrong input')
            show_admin_menu()
    except ValueError:
        print("Invalid input")
        show_admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_admin_menu()


@log_decorator
def payment_menu():
    text = '''
1. Show all payments
2. Payment
3. Withdraw money group
4. Withdraw money student
5. Back
    '''
    print(text)
    try:
        admin = Admin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Payment -> Show all\n')
            admin.show_all_payment()
            payment_menu()
        elif user_input == 2:
            print('\nHome -> Payment -> Payment\n')
            admin.payment_student()
            payment_menu()
        elif user_input == 3:
            print('\nHome -> Payment -> Withdraw group\n')
            admin.withdraw_payment_group()
            payment_menu()
        elif user_input == 4:
            print('\nHome -> Payment -> Withdraw student\n')
            admin.withdraw_payment_student()
            payment_menu()
        elif user_input == 5:
            show_admin_menu()
    except ValueError:
        print("Invalid input")
        payment_menu()
    except Exception as e:
        print(f'Error: {e}')
        payment_menu()


@log_decorator
def admin_teacher_menu():
    text = '''
1. Create teacher
2. Update teacher
3. Delete teacher
4. Show all teachers
5. Back
    '''
    print(text)
    try:
        admin = Admin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Teacher -> Create teacher\n')
            admin.create_teacher()
            admin_teacher_menu()
        elif user_input == 2:
            print('\nHome -> Teacher -> Update teacher\n')
            admin.update_teacher()
            admin_teacher_menu()
        elif user_input == 3:
            print('\nHome -> Teacher -> Delete teacher\n')
            admin.delete_group()
            admin_teacher_menu()
        elif user_input == 4:
            print('\nHome -> Teacher -> Show all teachers\n')
            admin.show_all_teacher()
            admin_teacher_menu()
        elif user_input == 5:
            show_admin_menu()
    except ValueError:
        print("Invalid input")
        admin_teacher_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_teacher_menu()


# A function related to groups in the Admin menu
@log_decorator
def admin_group_menu():
    text = '''
1. Create Group
2. Delete Group
3. Show all groups
4. Back
    '''
    print(text)
    try:
        admin = Admin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Group -> Create group\n')
            admin.create_group()
            admin_group_menu()
        elif user_input == 2:
            print('\nHome -> Group -> Delete group\n')
            admin.delete_group()
            admin_group_menu()
        elif user_input == 3:
            print('\nHome -> Group -> Show all groups\n')
            admin.show_all_groups()
            admin_group_menu()
        elif user_input == 4:
            show_admin_menu()
        else:
            print('Wrong input')
            admin_group_menu()
    except ValueError:
        print("Invalid input")
        admin_group_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_group_menu()


# A function related to groups in the Student menu
@log_decorator
def admin_student_menu():
    text = '''
1. Create Student
2. Update Student
3. Delete Student
4. Show all students
5. Back
    '''
    print(text)
    try:
        admin = Admin()
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Student -> Create student\n')
            admin.create_student()
            admin_student_menu()
        elif user_input == 2:
            print('\nHome -> Student -> Update student\n')
            admin.update_student()
            admin_student_menu()
        elif user_input == 3:
            print('\nHome -> Student -> Delete student\n')
            admin.delete_group()
            admin_student_menu()
        elif user_input == 4:
            print('\nHome -> Student -> Show all students\n')
            admin.show_all_groups()
            admin_student_menu()
        elif user_input == 5:
            show_admin_menu()
        else:
            print("Wrong input")
            admin_student_menu()
    except ValueError:
        print("Invalid input")
        admin_student_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_student_menu()


# A function for teachers
@log_decorator
def show_teacher_menu():
    text = '''
1. Show all my groups
2. Search teachers by group name
3. Start lesson
4. Logout
    '''
    print(text)
    try:
        teacher = Teacher()
        choose_menu: int = int(input('Choose menu: '))
        if choose_menu == 1:
            print('\nHome -> My groups\n')
            teacher.my_groups()
            show_teacher_menu()
        elif choose_menu == 2:
            print('\nHome -> Search teacher\n')
            pass
        elif choose_menu == 3:
            print('\nHome -> Lesson\n')
            pass
        elif choose_menu == 4:
            print("Logout successful")
            auth.logout()
            show_auth()
        else:
            print("Wrong input")
            show_teacher_menu()
    except ValueError:
        print("Invalid input")
        show_teacher_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_teacher_menu()


# A function for student
@log_decorator
def show_student_menu():
    text = '''
1. Show all my groups
2. Profile
3. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            print("\nHome -> Show all")
            pass
        elif user_input == 2:
            print("\nHome -> Profile")
            pass
        elif user_input == 3:
            print('Logout successful')
            auth.logout()
            show_auth()
        else:
            print('Wrong input')
            show_student_menu()
    except ValueError:
        print("Invalid input")
        show_student_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_student_menu()


# run program
if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    show_auth()
