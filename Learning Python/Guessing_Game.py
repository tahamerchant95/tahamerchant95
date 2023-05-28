from random import randint

var1= randint(1,100)

guesses=[]

print("Welcome to our number guessing game")


while True:
    player= int(input("Enter your first guess: "))

    if player < 1 or player > 100:
        print("Your guess is out of bounds, try again")
        continue
    
    if player == var1 :
        print(f'Congrats on guessing it write, guessed only in{len(guesses)} Guesses')
        break

    guesses.append(player)

    if guesses[-2]:
        if abs(var1-player) < abs(var1-guesses[-2]):
            print('Warmer')
        else:
            print('Colder')
    else:
        if abs(var1-player) <= 10:
            print('Warm')
        else:
            print('Cold')