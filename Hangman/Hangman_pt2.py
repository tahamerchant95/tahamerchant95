secret_word = ("python")

turns = 5

wrong_guesses= 0 

used_letters= []

dash_letter= "_" * len(secret_word)

while turns > 0 and dash_letter != secret_word:
    print("\nfollowing letters have been used:", used_letters)
    print("\nletters guessed currently:\t", dash_letter)
    guess= input("Enter guess letter:\t")
    guess= guess.lower()

    while guess in used_letters:
        used_letters.append(guess)
        print("Youve already used this letter:\t", guess)
        guess= input("Guess again:\t")
        guess=guess.lower()
    
    used_letters.append(guess)

    if guess in secret_word:
        print("Correct guess:",secret_word)
        new =""

        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                new = new + guess
            else:
                new = new + dash_letter[i]

        dash_letter = new

    if guess not in secret_word:
        print("\nWrong guess entered:")
        turns = turns - 1 
        print("\nTurns remaining:", turns)

        if turns == 0:
            print("Youve ran out of turns, \nthe secret word is:", secret_word)
        else:
            print("\n youve guessed the correct word:")


