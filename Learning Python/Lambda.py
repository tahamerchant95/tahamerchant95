# map function allows you to map function through iterable object

lst1= [1,2,3,4,5]

def square(nums):
    return nums**2 

print(list(map(square,lst1))) #can use map function to iterate over objects 


def text_func(text):
    if len(text) % 2 == 0 :
        return 'EVEN'
    else:
        return 'ODD'
    
my_text= ['This', 'is', 'a', 'normal', 'text']
print(list(map(text_func, my_text)))


# can use filter function to filter out results, for instance checking a list with even numbers to return True


def check_even(nums):
    if nums % 2 == 0:
        return nums
    
lst2= [0,1,2,3,4,5,6,7,8,9,10]

result= list(filter(check_even,lst2))

print(result)

#or to check for even numbers the other way we can do this so we can see the difference in code 

"""
num= [1,2,3,4,5,6,7,8,9,10]
def evens_check(nums):
    for nums in num:
        if nums % 2 == 0 :
            return nums 
        else:
            return 'ODD'
        
result1= evens_check(num)
print(result1)
"""


# will learn about lamba expressions now 
# lambda expressions can create functions wihtout using def 
# lambda uses single expression instead of block statements

def square(num): # basic function that sqaures a number, however can be coded in fewer lines
    result= num**2
    return result

print(square(2))

def squares(num): # see we removed a line and directly returned value 
    return num**2 

print(squares(4))


def sqrs(num) : return num**2 # have written entire code in one line 

result = lambda num : num ** 2 # removing the def and using lambda instead is a replication  of the def method
print(result(3))

print(sqrs(5))

# so now we can write out check evens function using lambda statement 

nums= [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda nums: nums % 2 == 0 , nums)))

print(list(map(lambda num: num**2 , nums)))


# for instance we need to gether the first letter of string 

def grab_string(text):
    result= text[0]
    return result

print(grab_string('Python'))

# make the code shorter

def grab_strings(text):
    return text[0]

print(grab_strings('Python'))

# can grab string using lambda function

ss= 'STRONG'

print(list(filter(lambda s : s[0], ss)))








