lst1= [1,2,3]

lst1.append(4) # adding element to list 

print(lst1)

print(lst1.count(10))

print(lst1.count(2)) # will return the number of times element occurs in list 


# there is a difference between append and extend methods 

# append() allows to append the whole object at the end 

lst1.append([4,5])

print(lst1)

lst1.extend([4,5]) # appends each element from the passed list as well, the major difference is this 

print(lst1)

print(lst1.index(2)) # returns the element at index value 


# insert(index,object) allows to specify the index where the value is to be placed

lst2= [1,2,3]

lst2.insert(2,'Python') # have inserted a string at index 2 

print(lst2)

lst2.pop(2) # popped the third element from the list or can also be said to remove element from second index 

print(lst2)

lst1.append('Python')
print(lst1)

lst1.remove('Python') # will remove element first occured in list 
print(lst1)

lst1.remove([4,5])
print(lst1)

lst1.reverse() # reversing the list, changes will be permanenent 
print(lst1)

lst1.sort() # from lowest to highest value
print(lst1)

# using reverse, there is an optional arguement as well

lst1.sort(reverse=True)

print(lst1)


# proper assignments need to be taking into consideration

x= 'Python Programming'

y= x.upper()

print(y)

# however it doesnt work with lists

a= [1,2,3]

b= a.append(4) # when you do this, this will return none value, affects the list

print(b)

b= a.copy() # hence we will need to make a copy of our list and then append the value we need 
b.append(4)
print(b)


print(a)
print(b)