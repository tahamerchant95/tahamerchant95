#using dictionaries help to map objects 

#dictionary holds a key and a value assigned to it 

first_dict= {'key1': 'Apple', 'Key2': 'Oranges', 'Key3': 'Mangoes'} #assigning three keys to their values 

print(first_dict)
print(type(first_dict)) #keep checking the type if not sure what data type is being used 

print(first_dict['key1']) #if want to know value of first key 


#dictionaries can hold various data types 

second_dict={'Key1': 'Strawberry', 'Key2': 123, 'Key3': [1,2,3,4]}

print(second_dict['Key3'][:-1]) #calling out last three values from key3 index pairing 

print(second_dict['Key1'].upper()) #can call functions as well on key values 

print(second_dict['Key3'].pop()) #trying to pop last value from the third key of the third index 
second_dict['Key2']= second_dict['Key2'] - 123 #can change values in key pairings 

second_dict['Key2']= second_dict['Key2'] =+ 123 # can use built in operators to add values 


print(second_dict)

#key pairing can be assigned by creating an empty dictionary instead of using key value arguements


d= {} # creating empty dictionary 

d['Fruit']= 'Mangoes' #assigning a key and its value through assignment 

d['Quantity']= 3 

print(d)


#dictionaries can be nested as well 

b= {'k1':{'k2':{'k3':'value'}}} #getting the key value through nested dictionary 

print(b['k1']['k2']['k3'])