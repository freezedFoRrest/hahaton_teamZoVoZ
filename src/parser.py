class Letter:
    def __init__(self, receiver, sender, date, subject, data, file_name):
        self.receiver = receiver
        self.sender = sender
        self.date = date
        self.subject = subject
        self.data = data
        self.name = file_name

class Parser:
    def __init__(self, file_path, extension):
        self.receiver = None
        self.sender = None
        self.date = None
        self.subject = None
        self.main_body = []
        self.file_name = file_path.name
        self.extension = extension
        self.letter = None
        if self.extension == ".txt":
            self.parse_txt()