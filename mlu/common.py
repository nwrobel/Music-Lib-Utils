import os
from os import listdir
from os.path import isdir, join

def getAllFilesRecursive(rootPath):
    
    allFiles = []
    
    for path, subdirs, files in os.walk(rootPath):
        for name in files:
            theFile = os.path.join(path, name)
            allFiles.append(theFile)
            
    return allFiles

def getAllDirsDepth1(rootPath):
    #onlydirs = [f for f in listdir(rootPath) if isdir(join(rootPath, f))]
    x = []
    for dir in listdir(rootPath):
        x.append(join(rootPath, dir))
    return x

def getProjectRoot():
    return "/home/nick/workspace/mlu/"

    
