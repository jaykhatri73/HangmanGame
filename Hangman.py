import random


def hangman():
    # keeping few words in memory
    word_list = ['python', 'java', 'ruby', 'javascript', 'html', 'css']

    # choosing random word from the memory
    word = random.choice(word_list)
    guessed_letters = []

    # number of attempts
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    # main logic
    while tries > 0:
        guess = input("Guess a letter: ").lower()

        # validating given input
        if guess.isalpha() and len(guess) == 1:

           # same input repeat error
            if guess in guessed_letters:
                print("You already guessed that letter. Try again!")
                continue

            guessed_letters.append(guess)

            # correct letter from user
            if guess in word:
                print("Good guess!")
                print_word = ""
                for letter in word:
                    if letter in guessed_letters:
                        print_word += letter + " "
                    else:
                        print_word += "_ "
                print(print_word)

                # once user wins the game
                if "_" not in print_word:
                    print("Congratulations! You won!")
                    break
            else:
                tries -= 1
                print("Wrong guess!")
                print("Tries remaining:", tries)

        else:
            print("Invalid input. Please enter a single letter.")

    else:
        print("You lost! The word was", word)


hangman()
