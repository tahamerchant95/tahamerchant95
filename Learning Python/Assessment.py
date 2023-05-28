# first exercise is to print only words that start with s 

st = 'Print only the words that start with s in this sentence'

for items in st.split(): #using split function to go through string
    if items[0] == 's': #using 0 index to specify start of the word with s 
        print(items)    


 # second exercise is to print all even numbers using range function
a=list(range(0,11,2))
print(a)

 # Third exercise is to use list comprehensions to create list of numbers divisible by 3 from 1 to 50 

lst1= [x for x in range(1,51) if x % 3 == 0]

print(lst1)

# Fourth exercise is to print all words that are even in length 
st = 'Print every word in this sentence that has an even number of letters'

for words in st.split():
    if len(words) % 2 == 0:
        print(words)

# Fifth exerise 
# print integers from 1 to 100
# multiples of three use "Fizz"
# multiples of five use "Buzz"
# multiple of both three and five use "FizzBuzz"

for letters in range(1,101):
        if letters % 3 == 0 and letters % 5 == 0:
            print("FizzBuzz")
        elif letters % 3 == 0 :
             print ("Fizz")
        elif letters % 5 == 0 :
             print("Buzz")
        else:
             print("Do nothing")
        

# create list comprehension to get first letters from every word in string
st = 'Create a list of the first letters of every word in this string'

lst2= [word[0] for word in st.split()]

print(lst2)
    
        