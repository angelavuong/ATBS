# Write a program that walks through a folder tree and searches for
# files with a certain file extension (such as .pdf or .jpg). Copy
# these files from whatever location they are in to a new folder.


import os, shutil, copyfile
import copyfile

for folderName, subfolders, filenames in os.walk('/Users/angvuong/atbs'):
    # print('The current folder is ' + folderName)
    for subfolder in subfolders:
        # print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            if filename.endswith('.py'):
                # print('FILE INSIDE ' + folderName + ': '+ filename)
                source = folderName + str('/') + filename
                print source
                if os.path.exists('/Users/angvuong/atbs/new_folder'):
                    shutil.copy(source, '/Users/angvuong/atbs/new_folder')
                else:
                    os.makedirs('/Users/angvuong/atbs/new_folder')
                    shutil.copy(source, '/Users/angvuong/atbs/new_folder')
