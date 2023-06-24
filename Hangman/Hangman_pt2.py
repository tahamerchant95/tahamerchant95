secret_word = ("python") # stored a word in our variable, this remains constant

turns = 5 # maximum number of turns allowed 

wrong_guesses= [] # currently wrong guesses are zero 

used_letters= [] # initialized an empty list 

dash_letter= "_" * len(secret_word) # this will print dashes with the number of letters in our word

# in this case we have 6 letters so will print 6 dashes

while turns > 0 and dash_letter != secret_word:
    print("\nfollowing letters have been used:", used_letters)
    print("\nletters guessed currently:\t", dash_letter)
    guess= input("Enter guess letter:\t")
    guess= guess.lower()

    if len(guess) != 1: # user enters single letter at a time 
        print("\nEnter single letter at a time:", guess)
    elif guess not in 'abcdefghijklmnopqrstuvwxyz': # user needs to only enter letters 
        print("\nenter only letter:", guess)

    while guess in used_letters:
        print("Youve already used this letter:\t", guess)
        guess= input("Guess again:\t")
        guess=guess.lower()
    used_letters.append(guess)

    if guess in secret_word:
        print("Correct guess:", guess)
        correct_letters =""

        for letters in range(len(secret_word)):
            if guess == secret_word[letters]:
                correct_letters = correct_letters + guess
            else:
                correct_letters = correct_letters + dash_letter[letters]
        dash_letter= correct_letters
    elif guess not in secret_word:
        print("\nincorrect guess:", guess)
        wrong_guesses.append(guess)
        turns = turns - 1 
        print("\nremaining number of turns are:", turns)
    else:
        continue
    '''
    elif guess not in secret_word:
        print("\nletters guessed currently:\t", dash_letter)
        guess=input("\nincorrect guess, please enter again:")
        guess=guess.lower()
        wrong_guesses.append(guess) # wrong guesses will be added to list 
        print(dash_letter)
        
        turns = turns - 1 
        print("\nTurns remaining:", turns)
    else:
        continue
'''
if turns == 0:
    print("\nYouve ran out of turns \nthe secret word is:", secret_word)
else:
    print("\nyouve guessed the correct word:", secret_word)