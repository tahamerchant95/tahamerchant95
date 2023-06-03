def gensquares(n):
    for nums in range(n):
        yield nums**2

for x in gensquares(10):
    print(x)

###########################################################
import random

from random import randint

def rand_num(low,high, n):
    for nums in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

s= 'Hello'

for letters in s: 
    print(s)

s= iter(s)
print(next(s))

