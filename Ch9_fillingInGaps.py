import os, re

file_prefix = raw_input('Enter a file prefix: ')
# user_input = spam001.txt
userRegex = re.compile(r'(^[a-zA-Z]+)(\d+)(.*)')
print (fileRegex.findall('spam001.txt'))


import os, re

print('Enter a string to look for: ')
userIn = input()

for filename in os.listdir(os.getcwd()):
file = re.compile(r'(^[A-Za-z]+)(\d*)(.*)')
compare = file.search(userIn)
#print(compare.group())
if compare.group() == filename:
print(filename)
# content = open(os.getcwd() + "\\" + filename, 'r')
# fileContentString = content.read()
# content.close()
# fileInAList = fileContentString.split(" ")
