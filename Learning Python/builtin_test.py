def words_lengths(phrase):
    return list(map(len, phrase.split()))


print(words_lengths("this is a string"))


from functools import reduce

def digits_to_num(digits):
    
    return reduce(lambda x,y: x*10 + y,digits)

print(digits_to_num([1,2,3,4,5]))



# using filter function to return list of words starting with  first letter


def filter_words(lst, letter):
    return list(filter(lambda word:word[0] == letter , lst))

words= ["Hi", 'ham', 'cat', 'host', 'hen', 'dog', 'merc']

print(filter_words(words, 'h'))


