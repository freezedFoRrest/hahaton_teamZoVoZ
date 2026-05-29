from pathlib import Path
from parser import Parser


class Processor:


    @staticmethod
    def read_directory(inbox_directory):
        result = []
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
            file, folder = current_parser.parse()
            result.append((file,folder))
        return result
