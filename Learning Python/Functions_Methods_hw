def vol(rad):
    return ((4/3)*(3.142)*(rad**3))

result=vol(2)
print(result)

def ran_check(num, low, high):
    if num in range(low,high + 1):
        print(' {} is in the range between {} and {}'.format(num, low, high))
    else:
        print("Number out of range!")


result = ran_check(5,3,7)

s= 'This is Python Programming Language'
def up_low(s):
    d= {"upper": 0, "lower":0}
    for letter in s:
        if letter.isupper():
            d["upper"] += 1 
        elif letter.islower():
            d["lower"] +=1
        else:
            pass

    print("the original string is", s)
    print("The number of characters in uppercase are", d["upper"])
    print("The number of characters in uppercase are", d["lower"])

result= up_low(s)
print(s)

def unq_lst(lst):
    x= []

    for items in lst:
        if items not in x:
            x.append(items)

    return x 

result=unq_lst([1,1,2,2,3,3,4,5,6,7,7])
print(result)

def multiply(nums):
    total = 1
    for items in nums:
        total = total * items 

    return total

print(multiply([1,2,3,4]))

# the replace method helps out with dealign with spaces
# .replace methid allows to get rid of spaces

def palindrome(s):
    s= s.replace(' ','')
    return s == s[::-1]

print(palindrome('nurses run'))

import string

def pangrams_func(str, alphabet=string.ascii_lowercase):
    alphabet= set(alphabet)

    str= str.replace(" ","")

    str=str.lower()

    str=set(str)

    return str == alphabet

print(pangrams_func("The quick brown fox jumps over the lazy dog"))
print(pangrams_func("Hello World"))