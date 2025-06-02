class FileWriter:
    @staticmethod
    def write_to_file(data):
        with open("user_report.txt", "w") as file:
            file.write(data)

class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.qualifications = []

    def set_qualifications(self, qualifications):
        self.qualifications = qualifications

    def report_format_user(self):
        report_string = self.firstName + " " + self.lastName + "\n"
        for qualification in self.qualifications:
            report_string += str(qualification) + "\n"

        return report_string

    def report_user(self):
        report_string = self.report_format_user()
        FileWriter.write_to_file(report_string)


if __name__ == "__main__":
    user = User("Steve", "Jobs")
    user.set_qualifications([10, 11, 15])
    user.report_user()
