# There are alot of python built in fucntions
# range() also to generate a list of integers instantly
# since range function is a 'generator' it requires a list function to get elements out of it 
# generator allows to get information but not store in memory 


print(range(0,5)) #generating a number of integers from 0 to 5 


print(list(range(0,5))) #casting range to list to get items, from zero upto 5 

#there are three parameters when it comes to defining range 
# starting value
# stop value 
# step size


a= list(range(0,10,2)) #have set step size to 2 

print(a)


position_count= 0 

#for items in 'Python':
#    print("At position {} the alphabet is {}".format(position_count, items))
#    position_count += 1 

# the above code can be written using the enumerate function as well
# enumerate allows us to know how many times the loop has gone through 

for p, alphabet in enumerate('Python'): #unpacked tuple 
    print('At position {} the alphabet is {}'.format(p,alphabet))

#enumerate results in a return of tuples in a list, hence we can unpack tuples as done in above code 


print(list(enumerate('Python')))


# the zip function is also a generator, can generate a list of tuples 

lst1= [1,2,3,4,5] #creating 2 lists 
lst2= ['a', 'b', 'c', 'd', 'e']

b= zip(lst1,lst2) # using zip function 

print(list(b))

for nums, alphabets in zip(lst1,lst2): #using zip to unpack tuples 
    print("First item was {} and second item was {}".format(nums,alphabets))

    
# in operator can be used to check whether elements exist inside object 
# can combine 'not' and 'in' opertors together 
x= 'x' in ['x', 'y', 'z'] #since x exists in list, will return True 

y= 'y' not in ['x', 'y', 'z']

print(x)

print(y)


# can check the min and max values in list 
# min= minimum value
# max= maximum value 



lst3= [20,21,34,45,54]

print(min(lst3))

print(max(lst3))

# using the 'random' library gives us a list of functions that can be imported
from random import shuffle

from random import randint

shuffle(lst3) #shuffling numbers 

print(lst3)

a= randint(0,10) # min and max values defined and random integer generated as we run code 

print(a)

# taking user input 

b= input("Lets try to take user input:") #input function allows to take user input 

print(b)




