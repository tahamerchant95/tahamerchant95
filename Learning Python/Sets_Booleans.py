# Some interesting facts about sets 
# 1. Sets are unordered collection of elements
# 2. Sets hold all unique elements
# 3. if there are x number of elements with unique values then using a set will remove duplication
# 4. using the add method only takes one arguement at a time
# 5. is you try to add multiple elements within an add statement it will give you TypeError s

a= set() # here we initialize empty set

a.add(6)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(1) #see if we try to add one more 1 it wont be added since sets contain unique values 

print(a)
print(type(a)) #checking the type of data structure used 

my_list= [1,1,1,1,3,3,3,4,5,6,7,7,7,9 ] #created a list
print(set(my_list)) #casted list into a set to give unique values 

c= None 
b= True #can set object to True or False value 

d=5
e= 6 

print("is %s greater than %s" %(d,e))
print(d > e )

print(c)
print(b)