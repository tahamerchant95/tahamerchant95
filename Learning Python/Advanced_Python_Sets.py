s= set() # creating a set object

s.add(1) # adding values to a set 

s.add(2)

print(s)

print(type(s)) # check type of set 

s.clear() # clears all elements in a set 

print(s)


s= {1,2,3}

sc= s.copy() # can make a copy of set 

print(s)

s.add(4) # added to set s but the copied set will not have the added value 

print(s)
print(sc)


print(s.difference(sc)) # this returns the difference of two sets 

s1= {1,2,3}
s2= {1,4,5}

s1.difference_update(s2) # will remove elements found in set2 and return set 1

print(s1)

s1.discard(1) # discarding elements from set 

print(s1)

s3= {6,7,8,9}
s4= {9,4,6,2}
s5 ={5}

s3.intersection(s4) # will check elements in both sets and return result if elements are common

print(s3)

s3.intersection_update(s4) # will filter out common elements between sets 
print(s3)


print(s3.isdisjoint(s4)) # will return true if two sets have null intersection

print(s3.isdisjoint(s5)) # since we know 5 doesnt exists in s3 so will return true

print(s3.issubset(s4)) # since 9 and 6 exists in both s3 and s4

print(s3.issubset(s5)) # will return false

print(s4.issuperset(s3)) # whether this set contains another set 

print(s3.issuperset(s5))

print(s3.symmetric_difference(s4)) # all elements that are exactly in one set

print(s3.union(s4)) # returns the union of two sets, all elements that are in either set

s3.update(s4) # updating the union set 

print(s3)
