import os

''' DO NOT MOVE THIS FILE LOCATION '''

DATABASE_PATH = 'PawlikLabs.db'


def getRootPath():
    absFilePath = os.path.abspath(__file__)
    fileDir = os.path.dirname(absFilePath)
    for i in range(2):
        fileDir = os.path.dirname(fileDir)
    return fileDir

def getDatabasePath():
    rootPath = getRootPath()
    return os.path.join(rootPath, DATABASE_PATH)