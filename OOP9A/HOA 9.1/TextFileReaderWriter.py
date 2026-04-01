from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        with open(self.file_path, 'r') as file:   # no encoding specified
            return file.read()

    def write(self, content: str):
        with open(self.file_path, 'w') as file:   # no encoding specified
            file.write(content)
