# coding: utf-8

import os
from os import listdir, sep
from os.path import isdir
from sys import argv


def tree(dir, tab, firstLevel=False):
    '''Print on the console the tree structure for an specific dir path.
    Args:
        dir: The dir of the root folder.
        tab: The tab caracter used for indent the root structure.
        firstLevel: Flag that indicates where the tree starts.
    '''

    files = listdir(dir)
    if firstLevel:
        print "."
    else:
        tab = "{0}   {1}".format("|", tab)
    i = 0
    filesCount = len(files)
    while i < filesCount:
        pathFolder = dir + sep + files[i]
        if i == filesCount - 1:
            print u'{0}{1}{2}'.format(tab, '└── '.decode('utf8'), files[i])
        else:
            print u'{0}{1}{2}'.format(tab, '├── '.decode('utf8'), files[i])
        if isdir(pathFolder):
            tree(pathFolder, tab)
        i = i + 1

if __name__ == "__main__":
    #format sample: python PTree.py C:\Users
    if len(argv) < 1:
        raise Exception("directory path is needed.")
    dir = argv[1]
    if not os.path.exists(dir):
        raise Exception("directory does not exist.")
    a = tree(dir, "", True)
