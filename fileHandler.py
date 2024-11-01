import os
import pickle
import datetime

from gif import Gif

APP_PATH_FILE = "./gifapp.config"
APP_FILE = "./gifapp.g"

def getGifPaths(path:str):
    array = []
    if not os.path.isabs(path):
        path = os.path.expanduser(f"~\{path}")
    for file in os.listdir(path):
        fullPath = path + "\\" + file
        if not os.path.isfile(fullPath):
            array.extend(getGifPaths(fullPath))
        if os.path.isfile(fullPath) and file.endswith(".gif"):
            array.append(fullPath)
    return array

def getTimes(path:str):
    try:
        return (datetime.datetime.fromtimestamp(os.path.getctime(path)), datetime.datetime.fromtimestamp(os.path.getmtime(path)))
    except Exception as e:
        print(e)

def getGifBytes(filePaths:list[str]):
    files = []
    for path in filePaths:
        try:
            with open(path, "rb") as file:
                files.append(file.read())
        except Exception as e:
            print(e)
    return files

def writeAppFile(gifs:list[Gif]):
    try:
#        with open(APP_PATH_FILE, "a") as file:
#            file.write(path)
        with open(APP_FILE, "wb") as gif_file:
            pickle.dump(gifs, gif_file)
    except Exception as e:
        print(e)

def readAppFile():
    try:
        with open(APP_FILE, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(e)
    return None

def readAppPath():
    try:
        with open(APP_PATH_FILE, "r") as file:
            return file.read().splitlines()
    except Exception as e:
        print(e)
    return None

def addPath(path:str):
    try:
        with open(APP_PATH_FILE, "a+") as file:
            if path not in file.read():
                file.write(f"{path}\n")
    except Exception as e:
        print(e)

def clearAppFiles():
    try:
        with open(APP_PATH_FILE, "w") as file:
            file.write("")
        with open(APP_FILE, "wb") as file:
            file.write(b"")
    except Exception as e:
        print(e)