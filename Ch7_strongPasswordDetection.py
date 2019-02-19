import re

lengthRegex = re.compile(r'.{8,}')
digitRegex = re.compile(r'\d+')
capitalRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]+')

flag = False
print('Please enter a password: ')
user_input = raw_input()

while (flag == False):
    if(lengthRegex.search(user_input) and digitRegex.search(user_input) and capitalRegex.search(user_input) and lowerRegex.search(user_input) != None):
        flag = True
        print('Thank you. Your password has been saved successfully!')
    else:
        print("Bad password! Please re-enter a different password: ")
        user_input = raw_input()
