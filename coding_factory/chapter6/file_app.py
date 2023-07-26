import sys
from pathlib import Path
import os

path = Path('C:/tmp/cf2023.txt')

def read_from_file(path):
    try:
        with open(path) as f:
            contents = f.read()
        return contents
    except OSError as e:
        print(e, file=sys.stderr)

def write_to_file(path, text):
    try:
        with open(path, 'a') as f:    #  'a' append
            f.write(text)
    except OSError as e:
        print("Error: could not write to file" , path, e)

# use os module

def delete_file(path):
    try:
        os.remove(path)
        print("File", path, "deleted successfully!")
    except OSError as e:
        print("Error: could not delete the file", path)

print(read_from_file(path))
write_to_file(path, "Hello again!\n")
print(read_from_file(path))

delete_file(path)