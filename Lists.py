example_list=[1,2,3,4] #creating a basic list consisting of 4 elements 

print(example_list)

print(len(example_list)) #getting number of items in the list


my_list=["Python", 12, 13.56, 'b'] #list can hold many data types

print(my_list)

print(example_list[0]) #example of slicing a list 

print(example_list[1:])

print(example_list[:2])

print(example_list[:-1]) #get everything except last item 


#lists are mutable, means anything can be added or removed from list 


example_list=example_list + my_list #lists can be concatentated
print(example_list)

#if want to add or append item to a list 

example_list=example_list + ['New item'] #to add changes to list will need to reassign variable to the list

print(example_list)

#for instance if i try to double the list and not reassign the list variable the changes wont be permanent


example_list*2 #as you can see I have called for the list to double itself but it hasnt since i havent assigned the variable to the list
print(example_list)


# some points of list to be noted
#1. python doesnt need to be specified list size
#2. no fixed type constraint, meaning list can hold many data types 

print(type(example_list)) # you can check the data type of the assigned variable, in our case its a list


example_list.append("Second Item") #can append item at the end of list and can be made permanent without reassignment 
print (example_list)

# to remove item from list, can use pop function
# however, using the pop removes the last item from the index by default
# if want to remove specific index will need to specify the actual index 


example_list.pop(7) #want to remove the second item from list 

print(example_list)
