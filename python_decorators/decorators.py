####
# First Class Objects
###
'''
In python, functions are first-class objects. This means that functions
can be passed around and used as arguments.
'''
def say_hello(name):
    return print(f"Hello {name}")

def be_awesome(name):
    return print(f"Yo {name}, together we are the best.")

def greet_bob(greeter_func):
    return greeter_func('Bob')

'''
Above, the functions say_hello() and be_awesome() are regular functions that expect a name
given as a string.
The greet_bob function does not expect a string, but rather a function.
'''
#greet_bob(say_hello)

'''
Note that the function that is passed does not have parentheses.
'''
###
# Inner Functions
###
'''
Functions can be defined inside other functions. This is called an
inner function. Below is an example.
'''
def parent():
    print('printing from the parent() function')

    def first_inner_function():
        print('printing from the first inner function')
    def second_inner_function():
        print('printing from the second inner function')

    second_inner_function()
    first_inner_function()

#parent()

'''
Note that inner functions are not defined until the parent function
is called. They are locally scoped to the parent() and so cannot 
be called outside of it.
'''
###
# Returning functions from functions
###
'''
Python allows you to use functions as return values. 
'''
def parent2(num):
    def first_inner_function2():
        return print('Hi I am julie')
    def second_inner_function2():
        return print('call me liam')
    
    if num == 1:
        return first_inner_function2
    else:
        return second_inner_function2

# This will NOT call the function, but rather save it to the variable
#function = parent2(1)

# This WILL call the function
#function()

###
# Simple decorators
###
def my_decorator(func):
    def wrapper():
        print('This is occurring before the function is called.')
        func()
        print('This is occurring after the function is called.')
    return wrapper

def say_whee():
    print('whee')

'''
In the example above, my_decorator gets passed a function,
then the inner function wrapper is defined and returned.
I am not sure why wrapper() doesn't need to be passed func().. 
'''
#say_whee_decorated = my_decorator(say_whee)
#say_whee_decorated()

# A second example

def my_decorator2(func):
    def wrapper():
        print('I am wrapping this function.')
        func()
        print('The function is wrapped.')
    return wrapper

def say_cool():
    print('cool')

#result = my_decorator2(say_cool)
#result()

###
# Decorators and Syntactic Sugar
###
'''
The above examples can be done more succinctly with syntactic sugar
using the @ symbol.
'''

def my_decorator3(func):
    def wrapper3():
        print('Before')
        func()
        print('After')
    return wrapper3

@my_decorator3
def wrap_me():
    print('wrap me!')

'''The @ symbol is basically like saying my_decorator3(wrap_me)'''
#wrapped = wrap_me()

###
# Reusing Decorators
###
'''
a decorator is just a regular python function.
'''
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def greet_person(name):
    print(f'hello {name}')

#result = greet_person('world')

''' The above will not work because the inner wrapper function
does not take any arguments. We fix this by using the *args and **kwargs
arguments. '''

def do_twice2(func):
    def wrapper_do_twice2(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice2

''' Now the inner function accepts any number of arguments
and passes them to the function it decorates'''

@do_twice2
def greet_person2(name, name2):
    print(f'hello {name}')

#greet_person2('bob', 'jim')
#greet_person2('', '')

###
# Returning values from decorated functions
###

@do_twice2
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'

#hi_adam = return_greeting('Adam')
#print(hi_adam)

''' When run, you see that hi_adam returns 'None'
 This is because the wrapper does not return a value.
 Let's rewrite the decorator function so it returns the 
 value of the decorated function.'''

def do_twice_return(func):
    def wrapper_do_twice3(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice3

@do_twice_return
def return_greeting_fixed(name):
    print('Creating greeting')
    return f'Hi {name}'

hi_adam = return_greeting_fixed('adam')
print(hi_adam)