# there is a difference between iteration and generation

# generator functions allow to return a value that can later be used to work with 

# generates a sequence of values over time

# main difference is to use the 'yield' syntax 

# when generator is compiled it becomes an object 

# genertor computes one value and then suspends activity 

# state suspension is a feature of generators 

def gen_cubes(n):
    for nums in range(n):
        yield nums**3

for x in gen_cubes(10):
    print(x)

def gen_fibo(n):
    a= 1 
    b = 1 

    for i in range(n):
        yield a 
        a,b= b, a + b

for nums in gen_fibo(10):
    print(nums)


# the above function can be written as a normal function as well

def fibo(n):
    a = 1 
    b = 1
    out= []


    for nums in range(n):
        out.append(a)
        a,b= b , a + b

    return out


fibo(10)

# next () allows to access next element in sequence
# iter() allows to support iteration where next doesnt allows it after it reaches true


def simp_gen():
    for x in range(3):
        yield x 

g = simp_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) #iteration will stop here since range is till 3 


s = 'Python'

for letters in s:
    print(letters)


iterate_string= iter(s)
next(iterate_string)
next(iterate_string)
next(iterate_string)
next(iterate_string)
