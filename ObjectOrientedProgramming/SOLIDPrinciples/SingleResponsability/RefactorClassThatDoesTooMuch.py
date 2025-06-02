# Original code (violates SRP)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_file(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.name}, {self.email}\n")


class FileWriter:
    @staticmethod
    def write_to_file(info):
        with open("users.txt", "a") as file:
            file.write(f"{info}\n")

class NewUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def format(self):
        return f"{self.name}, {self.email}\n"

    def save_to_file(self):
        formated_user = self.format()
        FileWriter.write_to_file(formated_user)

if __name__ == "__main__":
    user = NewUser("Steve", "Jobs")
    user.save_to_file()