import random


def hangman():
    word = random.choice(
        ["pugger", "littlepugger", "tiger", "superman", "thor", "pokemon", "avengers", "savewater", "earth", "annable"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10
    guessmade = ''

    turn = 10
    while turn > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character ")
            guess = input()

        if guess not in word:
            turn = turn - 1
            if turn == 9:
                print("9 turns left")
                print("  --------  ")
            if turn == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turn == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turn == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turn == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turn == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turn == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turn == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turn == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turn == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")


name = input("Enter your name ")
print("Welcome", name)
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
