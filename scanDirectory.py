# Scan directory and print the file names
import os

def scan(directory):
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                if entry.path.endswith(".txt"):
                    print(entry.name)
            else:
                scan(entry)
    except:
        print("Permission denied.")
scan("C:\\")

