from pathlib import Path

inbox_directory = Path(__file__).parent.parent / "inbox"

for letter in inbox_directory.iterdir():
    if letter.suffix == ".txt":
        pass
    if letter.suffix == ".json":
        pass
    if letter.suffix == ".jpeg":
        pass
    if letter.suffix == ".bin":
        pass