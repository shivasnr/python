# You’re not forced to a particular order in 
# which you supply your arguments—the name matters, not the position.
def f(*, a, b):
    print(a, b)

# f(1, 2) 
#f(a=1, b=2)


# Using * and ** for function arguments
# def f(a, b):
#     print(a, b)
# args = { "a": 1, "b": 2 }
# f(**args)

# def f(a, b, c):
#    print(a, b, c)
# l = [1, 2, 3]
# f(*l)

# Decorating your functions
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)
    return wrapper
@print_argument
def add_one(x):
    return x + 1
print(add_one(1))