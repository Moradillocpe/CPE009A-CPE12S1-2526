#Eunice E. Moradillo
class TextFileReaderWriter:
    def __init__(self, file_path: str):   
        self.file_path = file_path        

    def read(self) -> str:  # returns the content of the file as a string
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, content: str):  # overwrites the file content
        with open(self.file_path, 'w', encoding='utf-8') as file:  
            file.write(content)


if __name__ == "__main__":
    rw = TextFileReaderWriter("example.txt")

    # Write some content to the file
    rw.write("This is the supplementary task.")
    print("Written to file.")

    # Read the content of the file
    content = rw.read()   
    print("Read from file:")
    print(content)

    # Overwrite the file with new content
    rw.write("This content will overwrite the previous content.")
    print("\nFile overridden. New content written.")
    print(rw.read())
