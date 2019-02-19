import re

# Create dictionary and take user input
madlib_list = {}
user_adj = raw_input("Please provide an adjective: ")
user_noun = raw_input("Please provide a noun: ")
user_verb = raw_input("Please provide a verb: ")
user_noun2 = raw_input("Please provide a noun: ")

madlib_list = {
    "ADJECTIVE": user_adj,
    "NOUN": user_noun,
    "NOUN": user_noun2,
    "VERB": user_verb
}

# Open a READ file to view the madlib script, open a WRITE file to write new madlib!
file_read = open('/Users/angvuong/atbs/madLibs.txt','r+')
file_write = open('/Users/angvuong/atbs/madLibs_w.txt','w')
read_object = file_read.read()

# Find and replace matching dictionary values to the user input
pattern = re.compile(r'\b(' + '|'.join(madlib_list.keys()) + r')\b')
result = pattern.sub(lambda x: madlib_list[x.group()], read_object)

# Write new madlib to text file
file_write.write(result)

print result

# Close your READ and WRITE file
file_read.close()
file_write.close()
