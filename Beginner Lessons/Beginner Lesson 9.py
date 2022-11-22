"""
2022-11-21
1444-رَبِيع ٱلْآخِرَة-27

File operation
"""

# open the file
# to do anything with file we need to open file stream

file = open('myfile.txt', 'r')  # ('name', 'access method')
# basic access method {W = writing, R = reading, A= appending}


file.close()  # closing the stream - need to be close as well after use == manual method
# we do file.close or flush because it saves the change


# with open method
# if you want to use file once and close it automatically after use

with open('myfile.txt', 'r') as f:
    content = f.read()  # copying the document as string

print(content)

# overwriting the txt (write)

file = open('myfile.txt', 'w')
file.write('elo Im chiku')
file.close()

# extra fun fact - we are permissible to 'w' file that doesn't exist but not the 'r'

# adding the txt (append)
file = open('myfile.txt', 'a')
file.write("\noriginal text is gone :(")
file.flush()

# make/ assign files

from os import *  # using a module * == everything.

mkdir('test')  # mk - dir = make directory + only usable once == will terminate after one use

chdir('test')  # ch - dir = change directory == assigning which directory you want to work with
mkdir('mini test')  # makes the directory in the assigned one

# rename/ remove files

# rename('myfile.txt','moy man file ') -> before doing this you have to assign(change) directory back

# remove('moy man file)


"""
quick 日記
for some reason when I use these file.write method
I cannot put korean or special character in it  ಥ﹏ಥ
"""
