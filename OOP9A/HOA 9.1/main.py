from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter

# Test the default class
df = FileReaderWriter()
df.read()
df.write()

# Test the CSV class
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["bye"])

# Test the JSON class
j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo', {'bar': ('baz', None, 1.0, 2)}], filepath="sample2.json")

# Test the TextFileReaderWriter
t = TextFileReaderWriter("sample.txt")
t.write("hello,bye")
print("Written to file.")
print(t.read())
