# decorators modify the functilality of another function

# makes code shorter 

def func():
    return 1

print(func())

s= "Is a Global Variable"

def chk_for_locals():
    print(locals())

print(locals()) # checking local variables
print(globals()) # checking global variables

print(globals().keys()) #check for keys 

print(globals()['s']) # checking if s variable is global

print(chk_for_locals()) # no local variables found in function


# in pythonn everything is an object 
'''
def greeting(name='Merchant'):
    return 'Hello ' + name

print(greeting())

del greeting

greeting() # will produce error even after we have deleted greeting function
'''
# we can treat functions as objects 
# fucntions are objects that can be passed on to other objects 


def hello(name='Merchant'):
    print(' The hello() function is executed')

    def greet():
        return '\t this is inside greet() function'
    
    def welcome():
        return '\t this is inside welcome() function'
    
    print(greet())
    print(welcome())
    print("now we are back inside hello() function")


print(hello())

# can return functions from within functions 

def hello(name='Merchant'):

    def greet():
        return '\t this is inside greet() func'
    
    def welcome():
        return '\t this is inside welcome() func'
    
    if name == 'Merchant':
        return greet # if will put paranthesis the function will be executed 
    else:
        return welcome
    
a= hello()
print(a)

# creating a simple decorator example

def new_decorator(func):
    def wrap_func():
        print("code would be here, before func is executed")

        func()

        print("code will be here after func() executed")

    return wrap_func()


def func_needs_decorator():
    print("this function is in need of a decorator")

func_needs_decorator= new_decorator(func_needs_decorator)

func_needs_decorator # wrapped function and modified behaviour

@new_decorator
def func_needs_decorator():
    print("this function is in need of a decorator")

func_needs_decorator()


