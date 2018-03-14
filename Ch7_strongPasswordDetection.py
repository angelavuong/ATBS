import re

def passwordDetection():
    # word_count = len(password)
    # if(word_count) < 8:
    #     Print("Error: your password must be 8 characters long!")
    #     exit()
    pass


regex = re.compile(r'[a-zA-Z0-9_]')
if (regex.search('aalaksjgljasa') == None):
    print("Good password")
else:
    print "Bad password!"
