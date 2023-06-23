# we will create the hangman game
# the game takes in a secret word 
# user needs to guess the word by passing letters
# user inputs letter guesses and game checks whether the letter is in string 
# need to prompt user if the guess is correct/incorrect
# user will get a set number of chances to guess letters 
# when user guesses all correct letters user wins 
# if user looses all chances game ends and secret word is printed out 
# what if user enters the same letter again 

secret_word=('python') #we have set the secret word for user to guess

allowed_turns= 5 # user gets 5 chances to guess word

guesses=[] # have assigned an empty variable which will be appended whe user guesses any letter

already_guessed=[]

while allowed_turns > 0 : # will run when allowed turns are greater 
    failed = 0 

    for letters in secret_word: # will check for characters in our provided word 
        if letters in guesses: # will check if letters exists in guesses
            print(letters, end="")      
        elif letters in already_guessed:
            print("Youve already guessed that letters, enter another")
        else:
            print("_", end="")
            failed= failed + 1

    if failed == 0:
        print("\nYouve guessed the correct word")
        break

    guess=input("\nGuess a character:")
    guesses.append(guess)
    already_guessed.append(guesses)

    for letters in already_guessed:
        if letters in already_guessed == guesses:
            print("\nyouve already guessed this letter:")

    if guess not in secret_word:
        allowed_turns= allowed_turns - 1 # decrease the number of turns 
        print("\nWrong guess! "  +  " turns remaining:", allowed_turns)
        if allowed_turns == 0 :
            print("\nyou lose")

