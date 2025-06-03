import json
from abc import ABC, abstractmethod

# You're generating reports in JSON format. Later, you want to support XML and CSV
class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def output(self, format):
        if format == "json":
            # JSON output logic
            pass
        elif format == "xml":
            # XML output logic
            pass

class Formatter(ABC):
    @abstractmethod
    def format(self, title, data):
        pass

class JsonFormatter(Formatter):
    def format(self, title, data):
        print("json formatted")

class XmlFormatter(Formatter):
    def format(self, title, data):
        print("xml formatted")

class NewReport:
    def __init__(self, title, data, formater):
        self.title = title
        self.data = data
        self.formater = formater

    def output(self):
        self.formater.format(self.title, self.data)


if __name__ == "__main__":
    new_report = NewReport("Title", "Data", JsonFormatter())
    new_report.output()

    new_report.formater = XmlFormatter()
    new_report.output()