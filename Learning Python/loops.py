# if-else allows to specify multiple conditions
# if condition1 happens then do something
# else if condition 2 happens do something
# else do nothing 
# indentation is really important when it comes to check conditions and executing loops



if True:
    print('statement is true ')


fruit= 'Apple' #assinging a variable with value Apple

if fruit == 'Orange': #if condition one false move to next condition
    print('color of orange is orange')
elif fruit =='Apple': #if condition two true execute this statement
    print("color of Apple is red")
else:
    print("No fruits are available to buy") #final condition



# for loops help to iterate over items
# can iterate over strings, tuples, lists, keys, and values 


lst1= [1,2,3,4,5,6,7,8,9] #created a list 

for numbers in lst1: #iteration using for loop
    print(numbers)


print (18%5) #using modulo allows us to get remainder value, 18 divided by 5 gives a remainder of 3


#we will try to find even numbers in our list that we have created
#we can know even numbers when a number is fully divisible giving a remainder of zero 

for numbers in lst1: #this allows us to use a for loop to iterate over list and specifiy a condition using if
    if numbers % 2 == 0 :
        print(numbers)
    else:
        print("Number is odd")


lst_sum= 0 

for numbers in lst1:
    #lst_sum= lst_sum + numbers #performing addition of all elements in the list 

    lst_sum += numbers #another way of doing this using comparison operators

print(lst_sum)


for items in 'Python': #using strings with for loop to iterate in sequence 
    print(items)


sample= (5,4,3,2,1)

for items in sample:
    print(items)

# when using for loops with tuple, list containing tuples can be unpacked as well

sample1= [(1,2), (3,4), (5,6)] #creating a list contaning tuples 

for items in sample1: #first we try to print items in list
    print(items)

for (t1,t2) in sample1: #unpacking tuples 
    print(t2)

# for loops can also be used with dictionary values 

dict_1={'k1': 1, 'k2': 2, 'k3': 3}

print (dict_1.keys()) #print keys

print(dict_1.values()) # print values

print(dict_1.items()) # print items which also support iteration 

for k,v in dict_1: # using for loop to print keys and values 
    print(k)
    print(v)


print(list(dict_1.values())) #casting list to get values

print(list(dict_1.keys())) #casting list to get keys 

# dictionaries are unorderedd so will need to use sort function 


# A while loop will keep on executing a condition till it becomes true
# can add else condition until condition is true with the while loop in play 
# break: using this will break out of current loop 
# continue: will continue executing if condition is met 
# pass: wont do anything 

y= 0 

while y < 5:
    print('y is currently', y)
    print(' y is still less than 5, adding 1 to y')
    y += 1

    if y == 1 : 
        print("y is still at 1") 
    elif y == 2:
        print("y is still at 2 ")
    elif y == 3:
        print("y == 3, time to break the loop")
        break #breaking the loop since condition is met 
    else:
        print("continuing loop")
        continue


