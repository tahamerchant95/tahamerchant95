# list comprehensions can be used with dictionaries as well 

a={x:x**2 for x in range(10)} # can be written in dictionary format

print(a)

b= [x**2 for x in range(10)] # will produce same result as using list comprehensions
print(b)


# dictionaries can be iterated using keys(), values(), items()

dict1= {'k1':1,'k2': 2}

for keys in dict1.keys():
    print(keys)

for values in dict1.values():
    print(values)

for items in dict1.items():
    print(items)

k_view= dict1.keys() # view is tied to original dictionary 

print(k_view) # can view the dictionary according to list type


dict1['k3']= 3 # adding a key to dictionary 

print(dict1)

print(k_view)

