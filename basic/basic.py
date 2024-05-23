x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
print(5/4)

# variables
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#strings
string = 'hello'
print(string)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)