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