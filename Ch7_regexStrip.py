import re



print("Please enter your string: ")
str_string = raw_input() # Appends the string to the list
print("Please enter your argument (ENTER if no parameters): ")
str_strip = raw_input() # Appends the argument to the list


if(str_strip == ''): # NULL parameter
    print(re.sub(r'(^\s*)(.*?)(\s*$)', r'\2', str_string))
else:
    # value = re.sub(r'(^\s*)(.*?)(\s*$)', r'\2', str_string)
    print(re.sub(r'^[' + str_strip + ']+(.*?)[' + str_strip + ']*$',r'\1', str_string))
