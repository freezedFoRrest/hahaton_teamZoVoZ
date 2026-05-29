class Letter:
    def __init__(self, receiver, sender, date, subject, main_body, file_name):
        self.receiver = receiver
        self.sender = sender
        self.date = date
        self.subject = subject
        self.main_body = main_body
        self.name = file_name

class Parser:
    def __init__(self, file_path):
        self.receiver = None
        self.sender = None
        self.date = None
        self.file_path = file_path
        self.subject = None
        self.main_body = []
        self.file_name = file_path.name
        self.extension = extension
        self.letter = None


    def parse(self, extension):
        if extension == ".txt":
            self.parse_txt()
        elif extension == ".json":
            self.parse_json()

    def parse_txt(self):
        try:
            with (open(self.file_path, 'r', encoding='utf-8') as file):
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
    
    def parse_json(self):
        try:
            with open (self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            self.sender = data.get("from") or data.get("From") or data.get("от кого") or data.get("От кого")
            self.receiver = data.get("To") or data.get("to") or data.get("Кому") or data.get("кому")
            self.date = data.get("Date") or data.get("date") or data.get("Дата") or data.get("дата")
            self.subject = data.get("Subject") or data.get("subject") or data.get("тема") or data.get("Тема")
            self.main_body = data.get("body") or data.get("Body") or data.get("текст")
            self.makeLetter()
        except FileNotFoundError:
            raise ValueError(f"Файл {self.file_name} не найден")

        except json.JSONDecodeError as e:
            raise ValueError(f"Не удалось разобрать JSON в файле {self.file_name}: {e}")

        except Exception as e:
            raise RuntimeError(f"Ошибка при разборе {self.file_name}: {e}")

    
    def makeLetter(self):
        letter = Letter(self.receiver, self.sender, self.date, self.subject, self.main_body, self.file_name)
        self.letter = letter