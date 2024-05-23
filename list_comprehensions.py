[x for x in range(1, 5)]

list(range(1,5))

[x + 4 for x in [10, 20]]

# Nested list comprehension
m = [[j for j in range(3)] for i in range(4)]
#print(m)

# Or, if you want to flatten the previous matrix:

n = [value 
     for sublist in m 
     for value in sublist
    ]
#print(n)

# Set comprehensions
# The syntax for a Python set comprehension is not much different. 
# We just use curly braces instead of square brackets:

# { <expression> for item in set if <conditional> }
s = {s for s in range(1,5) if s % 2}
print(s)

# A dictionary requires a key and a value. Otherwise, it’s the same trick again:
x = {x: x**2 for x in (2, 4, 6)}
print(x)
