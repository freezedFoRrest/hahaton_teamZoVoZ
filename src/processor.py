from pathlib import Path
# from parser import Parser


class Processor:
    def __init__(self):
        pass

    def read_directory(inbox_directory):
        current_parser = None
        for letter in inbox_directory.iterdir():
            if letter.suffix == ".txt":
                current_parser = Parser(letter, 'txt')
            if letter.suffix == ".json":
                current_parser = Parser(letter, 'json')
            if letter.suffix == ".jpeg":
                current_parser = Parser(letter, 'jpeg')
            if letter.suffix == ".bin":
                current_parser = Parser(letter, 'bin')
            result = current_parser.parse()
            return result
