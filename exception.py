try:
    print(2/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# try:
#     # Open file in read-only mode
#     with open("not_here.txt", 'r') as f:
#         f.write("Hello World!")
# except IOError as e:
#     print("An error occurred:", e)

try:
    # Open file in write-mode
    f = open("myfile.txt", 'w')
    f.write("Hello World!")
except IOError as e:
    print("An error occurred:", e)
finally:
    print("Closing the file now")
    f.close()