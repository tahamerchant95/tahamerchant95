# map function is a built in library that takes two args
#  map returns an iterator 

# using map with lambda functions allows to save effort

def farenheight(celcius):
    return (9/5) * celcius + 32

temps=[0,20,30]

f_temps= map(farenheight,temps) # can use map using this statement
print(list(f_temps))


a=[1,2,3]
b=[4,5,6]
c= [7,8,9]

print(list(map(lambda x,y,z: x + y + z, a, b, c))) # or can simply use lambda with map 


# can use reduce function to reduce the value by adding two elements and coming to a single result

# the reduce function first applies to the first two elements

# when the first two elements are added the function moves on adding the answer recieved from the first two elements and then moves on to the next 

from functools import reduce

lst= [21,33,56,78]

a= reduce(lambda x, y: x + y, lst)
print(a)

max_value= lambda a ,b: a if (a >b) else b 
print(reduce(max_value, lst))

# filter function filters out elements when statement returns true 

# the filter function needs a function first as its arguement
# function needs to return a boolean value
# applied to every element of the iterable 
# also most commonyl used with lambda functions 

def even_check(nums):
    if nums % 2 == 0:
        return True
    
lst=range(20)
a=list(filter(even_check,lst))
print(a)

b= list(filter(lambda x: x % 2 == 0, lst)) # can use filter with lambda, will return same output 
print(b)

# zip performs as an aggregator by combining elements from each iterables
# with no arguements returns an empty iterator
# with 1 arguments returns 1-tuples

x= [1,2,3]
y =[4,5,6]

print(list(zip(x,y)))

# can zip dictionaries as well

a = {'a': 1, 'b': 2}
b=  {'c': 3, 'd': 4}

print(list(zip(a,b))) # this will print out only keys 
print(list(zip(a.values(),b.values()))) # this will print out values with respective keys 

# lets try to switch values with their keys 

def switch(a,b):
    reverse= {}

    for x,y in zip(a,b.values()):
        reverse[x] = y

    return reverse

print(switch(a,b))


# enumerate allows to keep count as you iterate 
# returns tuple in the form of (count, element)
# enumerate takes optional parameter of start to override default value of 0 

lst1 = [1,2,3]

#for x, y in enumerate(lst1):
  #  print(x)
 #   print(y)


for count, item in enumerate(lst1):
    if count >= 2: 
        break
    else:
        print(item)


months= ['Jan', 'Feb', 'March']

print(list(enumerate(months, start = 3)))

# all() function returns true if all values in the list are true
# any() will return true if any of the values in the list are true


lst3= [True, False, False, True]

print(all(lst3))
print(any(lst3))

# returns a complex number with real value + imag*1j
# coverts string or number to complex number
# if first param is a string will treat as compplex number
# second param cannot be a string

print(complex(1,2))
print(complex('12+2j'))

