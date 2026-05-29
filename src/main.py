from pathlib import Path
from processor import Processor

def find_directory(directory_name):
    directory = Path(__file__).parent.parent / directory_name
    return directory


inbox_directory = find_directory('inbox')
output_directory = find_directory('output')
result = Processor.read_directory(inbox_directory=inbox_directory)
for file, folder in result:
    path_to_directory = Path(output_directory) / folder
    if not path_to_directory.is_dir():
        path_to_directory.mkdir()
    file.rename(path_to_directory / file.name)