# import whole module
import hellouniverse
#hellouniverse.my_function()

# Importing specific parts of a Python module
from hellouniverse import my_function, age
hellouniverse.my_function()
print("My age: ", hellouniverse.age)

# Wildcard imports (are bad practice)
from hellouniverse import *

# Import aliases
import hellouniverse as universe