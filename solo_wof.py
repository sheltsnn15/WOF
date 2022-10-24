import random


# read and load phrases from phrases.txt
def get_phrases():
    phrases = []
    with open("phrases.txt", 'r') as file:
        for line in file:
            phrases.append(line.rstrip())
    # pick random ph
    random.shuffle(phrases)
    return phrases


# Main display
def main_display(vowels, consonants, word_to_guess):
    phrase = "".join(word_to_guess)
    print(f'---------------- Guess That Phrase Game -----------------')
    print(f'  {phrase:^{54}} ')
    print("                                                          ")
    print(f'     {"".join(vowels)}        {"".join(consonants)}          ')
    print(f'                                                         ')


# Ask user choice
def get_user_action():
    valid_choice = False
    correct = ['1', '2', '3', '4']
    while not valid_choice:
        print("\nMenu:")
        print("  1 - Guess a consonant.")
        print("  2 - Guess a vowel.")
        print("  3 - Solve the puzzle.")
        print("  4 - Quit the game.")
        choice = str(input("\nEnter the number of your choice: "))
        if choice in correct:
            valid_choice = True
        else:
            print(f"{choice} is an invalid choice.\n")
    return int(choice)


# This is where the user choice is directed
def action(choice, vowels, consonants, toGuess, secretSentence, sentence, vowelsPurchased, consonantsPicked):
    solved = False
    endGame = False
    if choice == 1:
        pick_consonant(consonants, vowels, toGuess, secretSentence,  consonantsPicked)
    elif choice == 2:
        pick_vowel(vowels, consonants, toGuess, secretSentence, vowelsPurchased, consonantsPicked)
    elif choice == 3:
        solved = solve(toGuess, sentence)
    elif choice == 4:
        endGame = True
        solved = True
    return  endGame, solved

# Ask user for consonant
def pick_consonant(consonants,toGuess, secretSentence, consonantsPicked):
    keepGoing = True
    if len(set(consonants)) == 1:
        print("There are no more consonants to choose.")
        keepGoing = False
    else:
        consonant = (str(input("Pick a consonant: "))).lower()
    no_consonants = 0
    while (consonant.upper() not in consonants) and keepGoing == True:
        if len(consonant) != 1:
            print("Please enter exactly one character.")
        elif consonant.upper() in consonantsPicked:
            print(f"The letter {consonant.upper()} has already been used.")
        else:
            print(f'The character {consonant} is not a letter.')
        consonant = (str(input("Pick a consonant: "))).lower()
    while consonant in secretSentence:
        index = secretSentence.index(consonant)
        toGuess[index] = consonant.upper()
        secretSentence[index] = ' '
        no_consonants += 1
    consonantsPicked.append(consonant.upper())
    consonants[consonants.index(consonant.upper())] = ' '
    if no_consonants == 1:
        print(f'There is {no_consonants} {consonant.upper()}.\n')
    elif no_consonants > 1:
        print(f"There are {no_consonants} {consonant.upper()}'s.\n")
    else:
        print(f"I'm sorry, there are no {consonant.upper()}'s.\n")


# Lets the user buy a vowel
def pick_vowel(vowels, toGuess, secretSentence, vowelsPurchased):
    no_vowel = 0
    keepGoing = True
    vowel = (str(input("Pick a vowel: "))).lower()
    while (vowel not in secretSentence) and (keepGoing == True):
        if vowel.upper() in vowels:
            print(f"I'm sorry, there are no {vowel.upper()}'s.\n")
            vowels[vowels.index(vowel.upper())] = ' '
            break
        elif len(vowel) != 1:
            print("Please enter exactly one character.")
        elif len(set(vowels)) == 1:
            print("There are no more vowels.")
            keepGoing = False
        elif vowel.upper() in vowelsPurchased:
            print(f'The letter {vowel.upper()} has already been picked.')
        else:
            print(f'The character {vowel} is not a letter.')
        vowel = (str(input("Pick a vowel: "))).lower()
    while vowel in secretSentence:
        index = secretSentence.index(vowel)
        toGuess[index] = vowel.upper()
        secretSentence[index] = ' '
        no_vowel += 1
    if no_vowel > 1:
        print(f"There are {no_vowel} {vowel.upper()}'s.\n")
    elif no_vowel == 1:
        print(f"There is {no_vowel} {vowel.upper()}.\n")

    if vowel.upper() in vowels:
        index = vowels.index(vowel.upper())
        vowels[index] = ' '
        vowelsPurchased.append(vowel.upper())


# Lets the user guess correct answer
def solve(toGuess, sentence, balance):
    print("Enter your solution.")
    print(f'  Clues: {"".join(toGuess)}')
    guess = (str(input("  Guess: "))).lower()
    if guess == sentence.lower():
        if balance < 1000:
            balance = 1000

        print("Ladies and gentlemen, we have a winner!")

    else:
        balance = 0
        print("I'm sorry. The correct solution was:")
        print(sentence.upper())

    return True, balance


def main():
    balanceTotal = 0
    endGame = False
    # greeting the user
    print("Welcome to Solo Wheel of Fortune!\n")
    while endGame == False:
        for round in range(1, 5):
            solved = False
            balance = 0
            # calling the list of phrases from the text files
            phrases = get_phrases()
            size = len(phrases)
            # selecting a phrase from the list 
            sentence = phrases[random.randint(0, size - 1)]
            toGuess = []
            secretSentence = []
            # defining vowels and consonants
            vowels = ["A", "E", "I", "O", "U"]
            consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
            vowels_guessed = []
            consonants_guessed = []
            balance = 0
            for letter in sentence:
                secretSentence.append(letter.lower())
                if letter == '-' or letter == '&' or letter == "'":
                    toGuess.append(letter)
                elif letter != ' ':
                    toGuess.append('_')
                else:
                    toGuess.append(' ')

            # One round of the game
            while not solved:
                main_display(vowels, consonants, toGuess)
                choice = get_user_action()
                balance, endGame, solved = action(choice, vowels, consonants, toGuess, secretSentence, sentence, vowels_guessed, consonants_guessed)

            balanceTotal = balanceTotal + balance
            balanceDisplay = "€{:,}".format(balance)
            print(f"\nYou earned {balanceDisplay} this round.\n")

            # Check if the games still has rounds left
            if endGame:
                break
            if round == 4:
                endGame = True
    # displaying the final results   
    print("Thanks for playing!")
    balanceDisplay = "€{:,}".format(balanceTotal)
    print(f'You earned a total of {balanceDisplay}.')


if __name__ == '__main__':
    main()
