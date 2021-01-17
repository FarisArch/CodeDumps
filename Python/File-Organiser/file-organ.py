import os
import shutil
directory = "/home/faris/Downloads/"
files = os.listdir(directory)
extentions = []
folder_scape = {}

for file in files:
    name, ext = os.path.splitext(directory + file)
    if len(ext) <= 6 and len(ext):
        extentions.append(ext)


extentions = set(extentions)
for ext in extentions:
    folder_scape[ext] = ext[1:].upper()


for File in os.listdir(directory):
    filename = directory + File
    name, ext = os.path.splitext(filename)
    if ext:
        if ext in folder_scape:
            folder = folder_scape[ext]
            try:
                os.mkdir(directory+folder)
            except Exception:
                pass
            shutil.move(filename, directory+folder)
        else:
            print(ext, "not found")

