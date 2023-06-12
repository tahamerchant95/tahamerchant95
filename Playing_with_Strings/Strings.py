# Strings can be used for various purposes 
# reversing 
# finding vowels
# checking if string is palindrome 
# count the number of words in string


def rev_sentence(chars):
    return (chars[::-1]) # reversing sentence 


a=rev_sentence('Python Programming')
print(a)

def cnt_vowels(sentence): # getting the total number of occurences per vowel 
    vowels= "aeiou"
    count={chars:0 for chars in vowels}
    
    for chars in sentence:
        if chars in vowels:
            count[chars] += 1
    
    return count

b= cnt_vowels('Python Programming')
print(b)

def total_vowels(sentence): # will be getting total number of vowels in sentence
    vowels= ["a", "e", "i", "o", "u"]
    count= 0 

    for chars in sentence:
        if chars in vowels:
            count= count + 1

    print("Total number of vowels in sentence is: ", count)

        
c= total_vowels("Python Programming")

def palindrome(sentence):
    return sentence[::-1]

s= palindrome("Python")
print(s)


