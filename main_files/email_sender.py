import datetime

from main_files.json_manager import user_manager


class EmailSender:
    def __init__(self):
        self.__smtp_server = 'smtp.gmail.com'
        self.__port = 587
        self.__sender_email = 'alamovasad@gmail.com'
        self.__password = 'npif pwxa awsb ytcq'
        self.__create_data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S').__str__()
        self.__receiver_emails = []

    def filter_receiver_emails(self, to_whom: str) -> None:
        all_users = user_manager.read()
        for user in all_users:
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

    def send_email(self, to_whom: str):
        pass
