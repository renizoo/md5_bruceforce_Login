import hashlib


class Register:

    def __init__(self, file_name):
        self.file_name = file_name

    def new_user(self):
        with open(self.file_name, 'w+') as file:
            file.write("user;password\n")
            while True:
                user = input("Enter username: ")
                password = input("Enter password: ")

                while len(password) > 4:
                    password = input("Enter a maximum of 4 characters for the password.\n")

                md5_hash = hashlib.md5(password.encode()).hexdigest()
                file.write((user + ";" + md5_hash + '\n'))

                option = input("Want add a new user? y/n\n")

                if option.lower() != 'y':
                    break
