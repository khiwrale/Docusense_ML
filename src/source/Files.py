import os

def files(path):
    try:
        if os.listdir(path)==[]:
            print('Folder is empty')
        else:
            return os.listdir(path)
    except:
        "None files are in folder"