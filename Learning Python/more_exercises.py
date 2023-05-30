# create function that displays list to users

def my_func1(mylist):
    print(mylist)

mylist= [1,2,3,4,5]
my_func1(mylist)


# create function that takes user input 

#result= int(input("please enter a value:"))
#print (result)
'''
def user_choice():

    choice = 'Wrong'

    while choice.isdigit() == False:
        choice= input("choose a number:")

        if choice.isdigit() == False :
            print("Please enter valid number: ")

    return int(choice)

print(user_choice())
'''
# need to valid user input
# such as checking whether the input is a digit or not 

def chk_choice():
    choice ='Wrong'

    within_range= False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please enter number between (0-10)")

        if choice.isdigit() == False:
            print("that is not a digit, please enter again")

        if choice.isdigit() == True :
            if int(choice) in range (0,10):
                within_range = True
            else:
                within_range = False

    return int(choice)


print(chk_choice())