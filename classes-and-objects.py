class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
my_object = MyClass()
print(my_object.variable)

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
print(my_object.function())

# init()
# The __init__() function, is a special function that is called when the class is being initiated. 
# It's used for assigning values in a class.

class NumberHolder:

   def __init__(self, number):
       self.number = number

number_object = NumberHolder(5)
print(number_object.number)

