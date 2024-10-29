import os

def getGifs(path:str):
    array = []
    if not os.path.isabs(path):
        path = os.path.expanduser(f"~\{path}")
    for file in os.listdir(path):
        fullPath = path + "\\" + file
        if not os.path.isfile(fullPath):
            array.extend(getGifs(fullPath))
        if os.path.isfile(fullPath) and file.endswith(".gif"):
            array.append(fullPath)
    return array

def getTimes(path:str):
    try:
        return (os.path.getctime(path), os.path.getmtime(path))
    except Exception as e:
        print(e)

def getBytes(filePaths:list[str]):
    files = []
    for path in filePaths:
        try:
            with open(path, "rb") as file:
                files.append(file.read())
        except Exception as e:
            print(e)
    return files