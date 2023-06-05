from collections import Counter

lst=[1,1,1,1,1,2,2,2,3,4,5,6,7,8,8,8,9]

print(Counter(lst))

s= "how how manyy many times does each each come come in the sentence the"

s= s.split()
print(Counter(s))

s = Counter(s)
print(s.most_common(2))
print(s.items())


# defaultdict is a dictionary-like object that has all method that a dictionary can perform

# takes in arguement 'default_factory' as default data type

from collections import defaultdict

d ={}

d= defaultdict(object)

print(d['One'])


for items in d:
    print(items)

d= defaultdict(lambda: 0) #initizlizing with default value 

print(d['one'])

# standard tuple can be used to access numerical indexes

t= (1,2,3)

print(t[0]) # if we need to access the first element in the tuple


# using 'namedtuple can be used to assign names and their index values 


from collections import namedtuple

Dog= namedtuple('Dog', ['Age', 'Breed', 'Color']) # passed object type Dog and then assigned attributes 

sasha= Dog(Age=3, Breed='szitzu', Color='White')

print(sasha.Age)
print(sasha.Breed)
print(sasha.Color)


f = open('practice.txt', 'w+')
f.write('test')
f.close()

import os 
import shutil # allows to moves files to different locations

print(os.getcwd()) # can get working directory by import os module

print(os.listdir())

#shutil.move('practice.txt', 'D:\\tahamerchant95\\Learning Python') # specifiy file name and directory to move in

print(os.listdir()) #checking whether file has been moved 

# using os module can provide some methods of removing files
# os.unlink(path) = deletes file in path provided
# os.rmdir(path)= deleted folder, but folder needs to be empty
# shutil.rmtree(path), removed all files and folders in path 
# the above methods make changes permanenetly and cannot be reversed
# use pip install send2trash 


import send2trash

#send2trash.send2trash('practice.txt') # will remove the file 

print (os.getcwd())

# can use datetime module to provide time information
# arguments to initialize time are optional 

import datetime

t= datetime.time(4,20,1)
'''
print(t)
print('hour', t.hour)
print('minutes', t.minute)
print('seconds', t.second)
print('ms', t.microsecond)
print('timezone', t.tzinfo)
print('early', datetime.time.min)
print('late', datetime.time.max)
print('resolution', datetime.time.resolution)

'''

current= datetime.date.today() #present time as of today
print(current)

print('ctime', current.ctime())
print('tuple', current.timetuple())
print('ordinal', current.toordinal())
print('Year', current.year)
print('Month', current.month)
print('Day', current.day)

# above are print statements of todays time and date values


# will demonstrate how to work with numbers

import math

val= 4.25

print(math.floor(val))
print(math.ceil(val))
print(round(val))

''' below statements are all math constants where values of such constants are fixed 
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
'''



# seeding allows to generate the same random numbers in series 

import random

print(random.randint(0,100))

print(random.seed(101))


lst= list(range(0,10))
print(lst)

# sample size allows to pick element more than once

x=random.choices(population= lst, k=10)
print(x)

y= random.sample(population=lst, k = 10) # setting sample size k = 10
print(y)

z = random.shuffle(lst) #shuffling list
print(z)

a=random.uniform(a=10.5, b= 12.5) # uniform distribution
print(a)

b= random.gauss(mu= 20.3, sigma=1) # normal, gaussian distribution 
print(b)
