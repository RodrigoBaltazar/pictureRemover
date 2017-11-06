#!/usr/bin/python

import glob

lista =  glob.glob("/ourFolderPathHere/*.jpg")

for item in lista:
    if item[0] == item[-1]:
        item += 1
    print "<div><img src='" + item + "' alt=''></div>"
