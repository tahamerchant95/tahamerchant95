first_tuple= (1,2,3,3,5,3,2,1)

print(first_tuple[1])

print(first_tuple[-1])
print(first_tuple)


#there are some basic tuple methods that can be used 
print(type(first_tuple))

print(first_tuple.index(1)) #can check where the number lies in what index, we are checking where 1 lies in what index

print(first_tuple.count(1)) #checking the number of times 1 appers in our tuple 

print(first_tuple)

# Point to be noted about tuples 
# tuples are IMMUTABLE!
# means once tuple is assigned values it cannot be changed or modified 

#print(first_tuple.append(0)) #try to remove this line of code and see what I'm talking about 

