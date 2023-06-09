# can work with numbers through advanced methods

a=hex(250) # will print hex value
print(a)

b= bin(250) # prints number in binary format 
print(b)

c= pow(3,2) # squaring number
print(c) # should give result as 9 

d= abs(3.5) # want to return absolute value for this function
print(d)

e= round(1.644,2) # using round function can round number according to precision
print(e)

# can also use the math library which has alot of builtin modules 

##################################################################

# strings have alot of function associated with it 

f= 'python programming'
print(f.capitalize()) # will capitalize the first letter as we do in plain English 

print(f.upper()) # convert all characters in the string to upper letters

print(f.lower()) # converts all characters to lower string 

print(f.count('p')) # return the number of occurences p has in given string 

print(f.find('p')) #returns the index where character is first found 

print(f.center(20,'z')) # can place a string in center between a provided string and certain length

print('Python\tProgramming'.expandtabs()) # will expand tab notations 

g= 'Java1'
print(g.isalnum()) # checks if all charaacters in the string are alphanumeric

print(g.isalpha()) # checks if all characters are alphabets, in our string it will return false

print(g.lower())
print(g.isspace()) # will return true if characters in s are white space 

print(g.istitle())
print((g.isupper())) # checks if all characters in string are upper case

print(g.endswith('1')) # checks if string ends with specified character in endswith()

print(g[:-1]) # removes last element and print strings, same as slicing a string 

print(g.split('J')) # split string at certain element and return list 

print(g.partition('a')) #







