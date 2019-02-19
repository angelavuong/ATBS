# Import the os module, for the os.walk function
import os, re, shutil, send2trash

counter = 0

# Set the directory you want to start from
rootDir = os.getcwd()

for dirName, suCbdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        cost = (os.path.getsize(dirName + '/' + fname))
        if cost >= 10000000:
            trash = (dirName + '/' + fname)
            print(trash)
            counter += 1
            send2trash.send2trash(trash)

print (str(counter) + ' file(s) were sent to your Recycle Bin.')
