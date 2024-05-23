# Using with open() in Python
# r	open file for reading (default)
# w	open file for writing, truncating the file first
# x	create a new file and open it for writing
# a	Open for writing, append to the end of the file if it exists already
# t	Text mode (the default), can be used in combination with rwxa
# b	Binary mode (as opposed to text mode), can be used in combination with rwxa
# +	open a disk file for updating (reading and writing)



# Python write file
# with open('text.txt', 'w') as f:
#     for i in range(1, 5):
#         f.write(str(i))

# Python append to a file
# with open('text.txt', 'a') as f:
#     for i in range(1, 5):
#         f.write(f'Appended: {i} \n')

# with open('text.txt') as f:
#     text = f.read()

# print(text)

# Use Python to check if file exists
import os
if os.path.isfile('text.txt'):
    print("It's a file")

# Use Python to check if a directory exists
if os.path.isdir('basic'):
    print("It's a directory")
#Create a directory
#os.mkdir('test_dir')
os.remove('myfile.txt')


# Move a file with shutil
import shutil
shutil.move('/cba/home/myfile.txt', '/cba/home/mydir')
# Move to a directory, keeping the name intact
shutil.move('/cba/home/myfile.txt', '/cba/homebackups/')

