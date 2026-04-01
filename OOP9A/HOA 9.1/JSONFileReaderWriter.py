#Eunice E. Moradillo
# JSONFileReaderWriter.py

from FileReaderWriter import FileReaderWriter
import json

class JSONFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, 'r') as readfile:
            data = json.load(readfile)
            print(data)
            return data

    def write(self, filepath, data):
        with open(filepath, 'w') as writefile:
            json.dump(obj=data, fp=writefile)