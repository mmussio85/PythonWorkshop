# coding: utf-8

from os import listdir, sep
from os.path import isdir
from sys import argv



def tree(dir, tab, firstLevel=False):
    files = listdir(dir)
    if firstLevel:
        print "."
    else:
        tab = "|" + "    "+ tab
    i = 0
    filesCount = len(files)
    while i < filesCount:
        pathFolder = dir + sep + files[i]
        if i == filesCount - 1:
            print tab + '└── '.decode('utf8') + files[i]
        else:
            print tab + '├── '.decode('utf8') + files[i]
        if isdir(pathFolder):
            tree(pathFolder, tab)
        i = i + 1

if __name__ == "__main__":
    #format sample: python PTree.py C:\Users
    dir = argv[1]
    tree(dir, "", True)