import os

directory_path = "/media/flash/Data/A_STUDY/"
contents = os.listdir(directory_path)

for item in contents:
    print(item)
