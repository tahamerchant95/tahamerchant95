# list comprehensions allow for advanced operations
# for instance a for loop can be used in a single python statement 


lst1= ['P', 'Y', 'T', 'H', 'O', 'N']

for items in lst1:
    print(items)

lst2=[ items for items in lst1] #single line using for loop 

print(lst2)


lst3= [y**2 for y in range(0,10)] #squaring all elements using for and range function

print(lst3)


lst4= [y for y in range(0,10) if  y % 2 == 0] #using for an if conditional to print even number from list 

print(lst4)


lst5= [z for z in range(0,10) if z % 2 != 0] # prints out odd numbers 

print(lst5)



# convert Celcius to farenheight 

celcius= [10,20,30,40]

farenheight= [((9/5)* temps+ 32) for temps in celcius] # basic formula 

print(farenheight)


#comprehensions can be listed as well


lst6= [x**3 for x in [x**3 for x in range(0,10)]]

print(lst6)


