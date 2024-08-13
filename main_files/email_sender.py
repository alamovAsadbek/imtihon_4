import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class EmailSender:
    def __init__(self):
        self.__smtp_server = 'smtp.gmail.com'
        self.__port = 587
        self.__sender_email = 'alamovasad@gmail.com'
        self.__password = 'npif pwxa awsb ytcq'
        self.__create_data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S').__str__()
        self.__receiver_emails = []

    # this function allows you to login to the mail
    @log_decorator
    def login_email(self):
        pass

    # This function sorts the mail to which mail should be sent
    @log_decorator
    def filter_receiver_emails(self, to_whom: str) -> None:
        all_users: dict = user_manager.read()
        for user in all_users.values():
            if user['role'] == 'student':
                if to_whom == 'all':
                    self.__receiver_emails.append(user['email'])
                elif to_whom == 'male':
                    if user['gender'] == 'male':
                        self.__receiver_emails.append(user['email'])
                elif to_whom == 'female':
                    if user['gender'] == 'female':
                        self.__receiver_emails.append(user['email'])
        return None

    # This function sends a message
    @log_decorator
    def send_email(self, to_whom: str):
        self.filter_receiver_emails(to_whom)
        print(self.__receiver_emails)

    # This function only sends messages to one mailbox
    @log_decorator
    def only_send_email(self, email: str):

        pass
