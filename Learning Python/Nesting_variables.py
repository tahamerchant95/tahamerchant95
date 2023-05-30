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
print(globals()) # can check global values
print(locals()) # can check local values 



