x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# boolean operator
name = "Shiva"
age = 23
if name == "Shiva" and age == 23:
    print("Your name is Shiva, and you are also 23 years old.")

if name == "Shiva" or name == "Chet":
    print("Your name is either %s or Rick." %name)

# in operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


# change this code
number = 18
second_number = ''
first_array = [1, 3, 4]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")