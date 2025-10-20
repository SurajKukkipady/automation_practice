#first class function
#a programming language is said to have first-class functions
# if it treats functions as first-class citizens.

#first class citizens (programming)
# a first class citizen is an entity that supports all the operations generally
# available to other entities. These operations typically include being passed as
# an argument, returned from a function, and assigned to a variable.

def square(x):
    return x * x

f = square

print(f)
print(square)  # Output: <function square at 0x...>

