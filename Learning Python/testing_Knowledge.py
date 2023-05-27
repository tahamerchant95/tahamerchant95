#here Im going to demonstarte some examples for basic coding concepts 


a= 3 * (7 + 5)
b= 4 + 7 * 11 
c= (7 -4) + 5 
d= 3 + 2.5 + 11 

print(a)
print(b)
print(c)
print(type(d)) #checking data type of result 


#check square root and square

e= 2**3
print(e)

#some string exercises

a= 'Hello'
print(a[1]) #using indexing to print e
print(a[::-1])  #reversing the string 
print(a[-1]) #getting last item from list 


lst1= [0,0,0]

lst3= [5,3,4,6,1]
lst3.sort() #using sort function to sort list values 

print(lst3)
print(lst1)

#d= {'Simple_key': 'hello'}

#print(d.values()) #can grab hello using values function
#print(d['Simple_key']) #second way to grab us through using key value 


#d= {'k1':{'k2': 'hello'}} #nested dictionary 

#print(d['k1']['k2']) #getting value from nested dictionary 

#d= {'k1': [{'nest_key': ['this is deep', ['hello']]}]} #tricy dictionary took me a while to solve

#print(d['k1'][0]['nest_key'][1])

d= {'k1': [1,2,{'k2': ['this is tricky', {'tough': [1,2,['hello']]}]}]} #very tough 

print(d['k1'][2]['k2'][1]['tough'][2]) #solution 

#can dictionaries be sorted?
# yes they can be sorted through their names and key values 


my_dict={'Taha': '27', 'Nabeel': '26', 'Aneela': '29'}

print(sorted(my_dict)) #will be sorted in alphabetical order 


lst4= [1,2,2,33,4,4, 11, 22, 3 , 3, 3]

print(set(lst4)) #casting list to set to get unique values


l_one= [1,2,[3,4]]

l_two= [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1']) #using comparison to chek true and false result




