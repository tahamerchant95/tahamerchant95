def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
a= lesser_of_two_evens(2,5)
print(a)


def animal_cracker(text):
    words= text.split()
    return words[0][0] == words[1][0]

b= animal_cracker('LevelHeaded Llama')
print(b)


def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20 :
        return True
    else:
        pass

    return False

c= makes_twenty(10,10)
d= makes_twenty(5,6)
print(d)
print(c)


def old_macdonald(name):
    if len(name) > 3 :
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'name is too short'

d= old_macdonald('macdonald')
print(d)

# the join function can be used to join words in list to a single piece of string 
def master_yoda(text):
    return ' '.join( text.split()[::-1])

e= master_yoda('name is taha')
print(e)

# check if number is within 10 if the given value between 100 and 200 
def almost_there(num):
    return (abs(100-num) <= 10) or (abs(200-num) <= 10) #using abs function to get absolute value 

b= almost_there(120)
print(b)

#every character in original string prints 3 times 
def paper_doll(text):

    result = ''

    for alphabets in text:
        result= result + alphabets * 3 
    
    return result

print(paper_doll("Taha"))

#simple blackjack code 
def black_jack(a,b,c):
    if sum((a,b,c)) <= 21 :
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
            final = sum((a,b,c)) - 10 
            return final 
    else:
        return 'BUST'
    
print(black_jack(3,4,5))

print(black_jack(10,12,5))

print(black_jack(10,11,5))