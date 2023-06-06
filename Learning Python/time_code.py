import time 


start_time= time.time() # getting start time
end_time= time.time() - start_time # calculating time it takes for code to finish

def func_one(n):
    return [str(num) for num in range(n)]

g= func_one(10)
print(g)

def func_two(num):
    return list(map(str,range(num)))

h= func_two(10)
print(h)

result= func_one(100)
print(result)

print(start_time)
print(end_time)

import timeit

stmt= 'func_one(100)'
setup = '''def func_one(n):
                return [str(num) for num in range(n)]'''

g=timeit.timeit(stmt, setup, number= 100000 )
print(g)

stmt2= 'func_two(100)'
setup2= ''' def func_two(nums):
                return list(map(str,range(nums)))
'''

h= timeit.timeit(stmt2, setup2, number= 100000)
print(h)