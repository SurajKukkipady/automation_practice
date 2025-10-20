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

print(f(5))     # Output: 25
print(square(5))  # Output: 25

print('************')

def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)  # Output: [1, 4, 9, 16, 25]

print('************')

def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message

log_hi = logger('Hi!')
log_hi()  # Output: Log: Hi!

print('************')

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Hello, World!')  # Output: <h1>Hello, World
print_h1('Welcome to Python!')  # Output: <h1>Welcome to Python!</h1>

print_p = html_tag('p')
print_p('This is a paragraph.')  # Output: <p>This is a paragraph.</

