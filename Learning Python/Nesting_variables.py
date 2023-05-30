#variables have a scope defined when coding 
# it ensures visibility in code 
# variable names are stored in namespace 


y = 50 

def numbers():
    y=40 
    return y 


print(numbers())

# there are four variable scopes
# local = names assigned within a function
# enclosing functions = namees in local scope and enclosing functions (def, lambda) inner to out 
# global= assigned at top level or declared global within the file 
# built in functions = name already assigned such as modules:len(), open()


#example of local function

nums= [1,2,3,4]

result = lambda x : x % 2 == 0 , nums # x is a local variable here 

print(result)


example = "This is a programming language"

def enc_func():
    example= 'Python' # example of an enclosing function where variable is local to enclosing function

    def enc_func1():
        print ('Programming' +example)

    enc_func1()

print(enc_func())

y = 10 

def loc_func(y):
    print("y right now is:" , y ) 

    y = 3 # variable name is local to a function sicne it doesnt have any enclosing functions
    print("changed value of y:", y)

loc_func(y)
print('y is still:', y)


y = 10

def glob_func():
    global y 

    print("have assingned y a global variable so y is:" , y)
    print(" you can see global variable value is:" , y)
    y = 5 # assigning a variable local to function but will change to global 

    print("Before running function variable should have value:", y) # here we see variable assigned value 5 since is local 
    
glob_func()
print("Value of y after running func is:" , y)
#print(globals()) # can check global values
#print(locals()) # can check local values 


# **kwargs and *args will be used at many places in python
# why ?
# we will write a simple function to explain this 


def my_func(a,b):
    return sum((a,b))

result=my_func(10,20)* .10 #returning 10 percent of the sum 
print(result)

# however we can pass multiple params in our function with assigned values

def my_func2(a=0, b=0, c= 0 ): #not an efficient way of producing results 
    return sum((a,b,c)) * 0.10

result=my_func2(10,20,30)
print(result)


# we will write the above code in efficient way using *args
# using args takes an arbitary number of arguements 
# takes them in values as tuples
# arbitary meaninig any random name 
# so if want to use any name that takes random values need to use * before word 

def my_func3(*args):
    return sum((args)) * 0.10 

result=my_func3(10,20) 
print(result) 


def my_func4(*nums):
    return sum((nums))*0.20

result=my_func4(10,20)
print(result)

# instead of creating tuple values we can use **kwargs
# kwargs allow to create dictionary values, meaning keys and values 

def my_func5(**kwargs):
    if 'product' in kwargs:
        print(f"My favourite product is {kwargs['product']}")
    else:
        print("Dont print anything")

result= my_func5(product='Mangoes')
print(result)
    
def my_func6(*args, **kwargs):
    if 'fruit' and 'shake' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May i have some {kwargs['shake']}, shake?")
    else:
        pass

result=my_func6('bread', 'omlette', fruit='Mangoes', shake= 'Juice')
print(result)
