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
            
    def parse_txt(self):
        try:
            with (open(self.name, 'r', encoding='utf-8') as file):
                for line in file:
                    line = line.strip()
                    if line.startswith("From:") or line.startswith("От кого:"):
                        self.sender = line[line.index(":")+1:].strip()
                    elif line.startswith("To:") or line.startswith("Кому:"):
                        self.receiver = line[line.index(":") + 1:].strip()
                    elif line.startswith("Date:") or line.startswith("Дата:"):
                        self.date = line[line.index(":") + 1:].strip()
                    elif line.startswith("Subject:") or line.startswith("Тема:"):
                        self.subject = line[line.index(":") + 1:].strip()
                    else:
                        self.main_body.append(line)
                self.makeLetter()

        except FileNotFoundError:
            raise ValueError(f"Файл {self.file_name} не найден")

        except UnicodeDecodeError:
            raise ValueError(f"Не удалось декодировать {self.file_name} - проверьте кодировку")

        except Exception as e:
            raise RuntimeError(f"Ошибка при разборе {self.file_name}: {e}")
    
    def makeLetter(self):
        letter = Letter(self.receiver, self.sender, self.date, self.subject, self.main_body, self.file_name)
        self.letter = letter