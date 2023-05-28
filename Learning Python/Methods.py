# Methods are functions built into objects 

# we will create a list consisting elements 

lst1= [1,2,3,4,5,2]

lst1.append(7) #add item to end of list

print(lst1.count(2)) # count number of times same item appears in list


print(lst1)

lst1.pop(3) #pop the fourth item from the list 

print(lst1)

#'help' is a built in python function to know what can functions do 


# functions help to not write same code again and again
# can be created once and called at multiple places
# uses def keyword and can insert parameters
# python uses docstrings to write some description about code

def add_text(): #example of a basic function 
    print('Python Programming')

add_text()

def input_name(name): #can pass in parameter such as Ive put name as a parameter to be passed
    print(f'My name is {name}')

input_name('Taha')

def addition_nums(n1,n2):
    return n1 + n2 #using return allows to store the result in variable names 

addition_nums(1,3)

result= addition_nums(1,3)
print(result)

print(addition_nums('Taha', 'Merchant'))

# difference between return and print
# return allows to save your result in a variable
# print just displays output 


def testing(a,b):
    print(a - b)

def testing_return(a, b):
    return a - b 

testing(3,1) #using print just displays result 

testing_return(3,1) #wont be able to see the output, but result is stored

result= testing_return(3,1) # as you can see answer was already stored and hence we assigned to variable name 
print(result)

result1= testing(3,1)
print(type(result1)) # since print doesnt store your result it will give nonetype object 
print(type(result))


# can write a function that checks for even numbers

def even_nums(number):
    return number % 2 == 0 

numbers=even_nums(20)
print(numbers)


def check_evens(lst1):
    for nums in lst1:
        if nums % 2 == 0 :
            return True
        else:
            pass # if got even number dont do anything 
    return False # return false if list doesnt have even numbers 
        
a= check_evens([1,2,3,4,5,6])
b= check_evens([3,5,7])
print(a)
print(b)
        


def chk_evens(lst1):

    evens= []

    for nums in lst1:
        if nums % 2 == 0 :
            evens.append(nums) #if even numbers found append to even list 
        else:
            pass
    
    return evens

a= chk_evens([1,2,3,4])
b= chk_evens([3,5,7,9])
print(a)
print(b)
        

fruits_stock= [('Apple', 100), ('Mangoes', 200), ('Bananas',  300)]

for items in fruits_stock:
    print(items) # example of functions returning tuples

for products, prices in fruits_stock: #tuple unpacking 
    print(products)

for products, prices in fruits_stock:
    print(prices)

lst2= [('Taha', 500), ('Merchant',400), ('Asad', 600)]

# function to display he top performed of the month 
def top_performer(lst2):

    max_hours= 0 

    employee_name= ''

    for employee, hours in lst2:
        if hours > max_hours :
            max_hours = hours
            employee_name= employee
        else:
            pass

    return (employee_name, max_hours)


a= top_performer(lst2)
print(a)

from random import shuffle
my_list= ['', 'O', ''] #this was the intial list 

def shuffle_list(my_list): #create function to shuffle list 
    shuffle(my_list)
    return my_list

def player_guess(): # created function to check if player guess is in play

    guess= ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1, or 2: ")

    return int(guess)


def check_guess(my_list, guess): # create fucntion to check guess in the play
    if my_list[guess] == 'O':
        print("Guess is correct")
    else:
        print("Better luck next time")
        print(my_list)


mixed_list=shuffle_list(my_list) #shuffling the list 

guess = player_guess() # taking users guess

check_guess(mixed_list, guess) # checking the guess on board 



