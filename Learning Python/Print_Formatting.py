#formatting strings can be done in various ways!

#through concatenation, fstrings, placeholders, pr=int formtting 


print("python  programming is growing  %s here" %'popular') #can use placeholders for formatting print statement

print("Python is utilized in many ways to interpret %s" %'data')


print("Using %s is a way of string %s" %('placeholders', 'formatting ')) #can place multiple elements through placeholders


a , b= 'placeholders' , 'formatting'

print("using %s can be used for string %s" %(a,b)) #variable names can be assigned for string formatting 


print("My name is %s" %'Merchant')
print("My name is %r" %'Merchant') #%r method inlcudes escape characters and quotation marks


print("Started to learn python %s" %'programming \ttoday') #%t used to add tabs in strings 


print("I had %s apples today" %4.75) #using %s operator will convert anything to string 

print("I had %d oranges today" %2.75) #using #d will convert numbers into integers before rounding them off


#will show an example of using multple formatting 

print("product: %s ,  Quantity: %5.2f , price: %1.0f, Taste: %r " %('Apple', 5.4566, 2.345, 'Yummy'))

#Using String Formatting 
print("an example of string  {} is to use format {}".format('formatting', 'method'))

print( '{2} {1} {0}'.format('Language', 'Programming', 'Python '))

print("Sheliza %s is Taha %s wife" %("Merchant", "Merchant")) #placeholders can do the same thing but can get duplication

print("Sheliza {p} is Taha {p} wife".format(p='Merchant')) #can avoid duplication using format method


#will try another way to format string using fstring formatting 

name='Taha'

print(f'he said his name is {name}. ')

print(f'he said his name is {name!r}') #can get string representation 
