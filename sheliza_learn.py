print("Hello World!") #printing hello world 

import sys #importing sys module which includes system files 

print(sys.version) #checking python version by importing system library and printing output 

if 5 > 2 :
    print("5 is greater than 2!") #demonstrating the importance of indentation 

#if 5 < 2 : 
#print("5 is not less than 2! ") # demonstrating incorrect form of indentation, will throw an indentation error 

if 3 > 4:
    print("3 is not greater than 4!") #same number of space needs to be specified in block of code 
    print("4 is greater than 3!")

x = 5 # variable assignment, storing value in a variable 
print(x)

"""
lines written between triple double quotes 
indicates multi line comments, meaning multiple
lines can be written between such quotes
"""


y = 10  #no need to declare variable data type 
y = "Test" #data type can be changed of the same variable, for instance y was integer value, then have changed to string value 
print(y)

a = int(3) #if want to declare data type can do this by "casting" for explicit decalration
b = str("test123")
c = float(3.5)

print(a,b,c)

print(type(a)) #printing out data type of variable "a"


a = "HAPPY"
#same output using double and single quotes for string
b= 'BIRTHDAY'

print(a,b)

A= "TO" #python is case sensitive, above declared value in variable 'a' will not be the same as value in 'A', hence result wont be overwritten

"""
_my_var = "YOU"
my_var1 = "MAY"
my_var2= "YOU"
my_var3 = "HAVE"
my_VAR= "MANY MORE"

1.Above declared are multiple variables
2.Variables can start with underscore, can contain Alpha-numeric characters (A-z, 0-9, and _ )
3.Cannot start with numbers 
4. cannot be python keywords
5. variable names are case-sensitve 

"""

"""
There are three types of variable casings
1. Camel Case: except for first word, all other words start with a capital letter
2. Pascal Case= all words start with a capital letter 
3. Snake Case= each word is separated by _ 
4. Choice of casing depends entirely on you!
5. why we use casing? for easy readable variable names
"""


myFirstVariable = "Camel Case" #camel case
MySecondVariable= "Pascal Case" #pascal case
MY_Third_Variable=  "Snake Case" #snake case

a , b , c = 1,2,3 #assigning many values to many variables
print(a,b,c)

a = b = c = -1 #assigning one value to multiple variables 
print(a)


multiple_fruits =["Apple", "Orange", "Banana"] #unpacking collection of items from lists and storing in variables
x , y , z = multiple_fruits
print(x)
print(y)
print(z)

x = "Happy"
y= "Birthday"
z = "To"
a = "You"

print(x,y,z,a) #printing multiple values in a single print statement 

print(x + y + z + a) # +operator can be used to output multiple variables 

b = 5
c = "Merch"

#print(b + c)  #Integers and strings cant be added together, will throw a TypeError

print(b,c) #to fix the TypeError in line 102, can use comma to separate variable output, adding comma supports different data types 

x = "running" #this variable has a global scope
def test_func():
    x="Testing" #this variable is local to the function 
    print("Test " +x)

test_func()

print("Test " +x)


def test_scope():
    global x #declaring a variable as global inside the function 
    x = "This is a global variable"
    print(x)

test_scope()


y = "Testing global variable"

def test_scoping():
    global y 
    y = "Python is awesome" #changing the value of a global variable, using global keyword inside the function can overwrite the previous value stored in variable declared outside function
    print(y)

test_scoping()

z = range(6) #using range data type to create a set from (0,6)
print(z)

z_values = {"name":"MERCHANT", "age":23} #created dictionary values 
print(z_values)

x_values = frozenset({"apple", "banana" , "Mango"}) #creating forzenset which is immutable
print(x_values)

a_values = b"Hello World" #bytes

b_values = bytearray(5) #creating array in bytes version
print(b_values)


c_values = memoryview(bytes(5)) #memoryview object 
print(c_values)


d_values = None #nonetype object 
print(d_values)


f_values = 3 + 5j #complex numbers, j is an imaginary part 
print(f_values)
print(type(x))

g_float = float(b) #converting value of b from int to float 
print(g_float)


h = 7.689
h_values = int(h) #converting from float to integer values 
print(h_values)


h_values= complex(h) #converting from float to complex value 
print(h_values)

#note: Cant convert from complex numbers to any number type lets try it in the below code 
"""
j_values = 7 + 5j
h_values = int(j_values) #will not be able to convert, will throw a typeerror 
print(h_values)

"""

import random 

print(random.randrange(1,9)) #there is not random function in python but has builtin module which can be imported through the random library



m = int("3") #casting string value to integer 
print(m)

n = float(3) #casting float value 
print(n)


h = "This is a random string" #strings in python represent unicode characters 
print(h[1]) 

for g in "Melon": #for loop going through all characters in strings 
    print(g)

print(len(h)) #printing number of letters in variable h (length)



txt = "Python is an \"easy to learn\" programming language" #insert double quotes inside a string 
print(txt)

txt2 = "an example of using \\ backslash"
print(txt2)

txt3 = "Hello\rSheliza" #carriage return example
print(txt3)

txt4 = "Hello \b\rSheliza you are the \bbest" #example of using backspace and carriage return
print(txt4)

#below are some examples of string methods 

print(txt2.capitalize())
print(txt.casefold())
print(txt2.center(1))
print(txt.count('a'))
print(txt4.encode())
print(txt4.endswith("best"))
print(txt4.expandtabs())
print(txt.find("Python"))
print(txt.upper())
print(txt.title())
print(txt.splitlines()) 
print(txt.startswith("P"))

x = "Taha Sheliza"
txt= x.strip() #returns string without any whitespace at beggining or end of line 
print(txt)

txt2= x.replace("T", "S") #replace specific value with something else 
print(txt2)

print(11 > 9) #will return boolean value (True or False)
print(9 > 11)
print( 11 == 9 )

a = 9
b = 7 

if b > a:
    print("b is greater than a".upper()) #adding a condtional loop to check what boolean value we get 
else:
    print("b is not greater than a".upper())


print(bool("Hello")) #evaluating value using bool function 
print(bool(12))


x = "Hello"
y = 1

print(bool(x))
print(bool(y))

#any string is true, except empty strings
#any integer is true, except the value 0 
#any list, tuple, set is true except empty 
#value none is false

class test_class(): #this is an example class
    def __len__(self): #this is a function 
        return 1 #returning 1 as value 
    
test = test_class() #object made from class
print(bool(test))


def my_funct(): #creating function that can return bool value
    return False

if my_funct():
    print("Yes") #if funtion returns YES will print true
else:
    print("NO") #if function returns NO will print False 

obj1 = my_funct()
print(obj1)

X = 100 
print(isinstance(X, int)) #builtin function returning a boolean value to determine data type of object 

y = "Sheliza"
print(isinstance(y , str)) #checking if datatype is string

z = 3.5
print(isinstance(y, float)) #checking if datatype is float 


















