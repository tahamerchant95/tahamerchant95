# regular expressions allow to check patterns in string

# for instance finding phone number in a document 


text= 'Programming in Python is 123-455-667'

print('Python' in text)

import re # importing regular expression libaray 

pattern = 'Python'

print(re.search(pattern, text)) # when printing regular expression we see that it prints a match object

match= re.search(pattern, text)

print(match.span())
print(match.start())
print(match.end())

text = 'Programming in python is easy because python is easy to understand'

match= re.search("python", text)

print(match.span()) # this will match the first instance

matches= re.findall("python", text) # this will find a list of all matches
print(matches)


print(len(matches))

# to get actual match objects can do something as coded below 


for match in re.finditer("python", text):
    print(match.span())

print(match.group()) #find actual text that matched 

# can use regular expressions to  find phone numbers or emails from string


text = 'My telephone number is 1111-2222-333'

phone= re.search(r'\d\d\d\d-\d\d\d\d-\d\d\d', text) # \d represents digits 

print(phone.group())

#however as we see the \d option has been used alot but can be too long for bigger strings
# hence, we use quantifiers in place 

phones= re.search(r'\d{4}-\d{4}-\d{3}', text) # this looks much simpler and clean
print(phones.group())


phone_pattern= re.compile(r'(\d{4})-(\d{4})-(\d{3})')

results= re.search(phone_pattern,text)

print(results.group())
print(results.group(1)) # can find out pattern by separating strings 
print(results.group(2))
print(results.group(3))

#list of identifiers
# 1. \d
# 2. \w alphanumeric 
# 3. \s whitespace 
# 4. \D nondigit
# 5. \W nonalphanumeric
# 6. \S non-whitespace


# list of quantifiers
# 1.  + occues one or more times 
# 2. {3} occurs exactly 3 times
# 3. {2,4} occurs two to  four times
# 4. {3,} occurs 3 or more times
# 5. \* occurs zero or more times
# 6. ? once or more

# can use regex with more additional syntax 

a=re.search(r"man|woman", "this is a man here") # can use the 'OR' operator
print(a)

b= re.search(r"man|woman", "this is a woman here")
print(b)

c= re.findall(r".at", "cat bat hat is here") # can use wildcard operator specified by using .period

print(c)

d= re.findall(r"...at", "cat bat hat splat plsat") #used modified regex to get five word letters contaning the letters at 

print(d)

# however we actually want the words that end with at 

e= re.findall(r'\S+at', "the bat went splat") # one or more non whitespace
print(e)

# cna use some more wildcard operators 
# $ = ends with 
# ^ = starts with 


f=re.findall(r'\d$', 'This ends with number 3')
print(f)

g= re.findall(r'^\d', '1 is the first number of the numeric sequence')
print(g)

text= "there are 3 numbers inside this string of 5 characters and 100 letters"

h= re.findall(r'[^\d]+', text) # exclude numbers in the string and print it out 
print(h)


proper= ' '.join(re.findall('[^!.?]+', text))
print(proper)

phrase= "find all non-hyphen words in this text-based string"

g= re.findall(r'[\w]+-[\w]+', phrase)
print(g)
