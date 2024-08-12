from main_files.auth import Auth
from main_files.decorator_func import log_decorator


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
            elif result_login['role'] == "admin":
                pass
        elif user_input == 2:
            pass
        else:
            print('Wrong input')
            show_auth()
    except ValueError:
        print("Invalid input")
        show_auth()
    except Exception as e:
        print(f'Error: {e}')
        show_auth()


@log_decorator
def show_admin_menu():
    text = '''
1. Group
2. Student
3. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
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
def show_teacher_menu():
    text = '''
1. Show all groups
2. Search teachers by group name
3. Start lesson
4. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            auth.logout()
            show_auth()
    except ValueError:
        print("Invalid input")
        show_teacher_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_teacher_menu()


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    show_auth()
