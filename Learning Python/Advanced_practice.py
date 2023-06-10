a= bin(1024)
print(a)

b= hex(1024)
print(b)

c=round(5.23222,2)

print(c)

s= 'hello how are you Mary, are you feeling okay'

print(s.islower())


s= 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))


set1= {2,3,1,5,6,8}
set2= {3,1,7,5,6,8}

print(set1.difference(set2))
print(set1.union(set2))

f= {x:x**3 for x in range(5)}
print(f)


lis1= [1,2,3,4]

lis1.reverse()

print(lis1)

lis2= [3,4,2,5,1]

lis2.sort()

print(lis2)