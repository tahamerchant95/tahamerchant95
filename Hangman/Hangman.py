# we will create the hangman game
# the game takes in a secret word 
# user needs to guess the word by passing letters
# user inputs letter guesses and game checks whether the letter is in string 
# need to prompt user if the guess is correct/incorrect
# user will get a set number of chances to guess letters 
# when user guesses all correct letters user wins 
# if user looses all chances game ends and secret word is printed out 


secret_word=('python') #we have set the secret word for user to guess

allowed_turns= 5 # user gets 5 chances to guess word

guesses='' # have assigned an empty variable which will be appended whe user guesses any letter

while allowed_turns > 0 :
    failed = 0 

    for letters in secret_word:
        if letters in guesses:
            print(letters, end="")
        else:
            print("_", end="")
            failed= failed + 1 

    if failed == 0:
        print("\nYouve guessed the correct word")
        break

    guess=input("\nGuess a character:")
    guesses = guesses + guess

    if guess not in secret_word:
        allowed_turns= allowed_turns - 1 
        print("\nWrong guess" + "turns remaining", allowed_turns)
        if allowed_turns == 0 :
            print("\nyou lose")




