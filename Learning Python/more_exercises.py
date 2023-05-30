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
'''
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

'''

game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list")
    print(game_list)


def user_pos():

    choice = 'Wrong'

    while choice not in ['0', '1' , '2'] : 
        choice=input(("Please pick position to replace (0,1,2): "))

        if choice not in ['0', '1', '2']:
            print("Sorry but you didnt enter any position")

    return int(choice)


def replace_choice(game_lst, position):
    user_placement= input("Type a string to place at position")

    game_lst[position] = user_placement

    return game_lst

def gameon_choice():

    choice= 'Wrong'

    while choice not in ['Y', 'N']:
        choice = input("Would you like to continue more? ")

        if choice not in ['Y', 'N']:
            print("You did not enter right choice")

    if choice == 'Y':
        return True
    else:
        return False
    

game_on= True

game_list= [0,1,2]


while game_on:
    display_game(game_list)

    position= user_pos()

    game_list= replace_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()

