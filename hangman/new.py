import random


# Picks a sentence randomly from the file phrases.txt
def load_phrases():
    lines = []
    with open("phrases.txt", 'r') as file:
        for line in file:
            lines.append(line.rstrip())
    # randomizing the elements in the list
    random.shuffle(lines)
    return lines


# Main display
def display(vowels, consonants, round, toGuess, prize):
    sentenceToDisplay = "".join(toGuess)
    amount = "${:,}".format(prize)
    print(f':: Solo WoF :::::::::::::::::::::::::::::: Round {round} of 4 ::')
    print(f'::{sentenceToDisplay:^{54}}::')
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(f'::   {"".join(vowels)}   ::   {"".join(consonants)}   ::  {amount:>9} ::')
    print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# Ask user choice
def getChoice():
    correctChoice = False
    correct = ['1', '2', '3', '4']
    while (correctChoice == False):
        print("\nMenu:")
        print("  1 - Spin the wheel.")
        print("  2 - Buy a vowel.")
        print("  3 - Solve the puzzle.")
        print("  4 - Quit the game.")
        choice = str(input("\nEnter the number of your choice: "))
        if (choice in correct):
            correctChoice = True
        else:
            print(f"{choice} is an invalid choice.\n")
    return int(choice)


# This is where the user choice is directed
def action(choice, balance, balanceTotal, vowels, consonants, toGuess, secretSentence, sentence, vowelsPurchased, consonantsPicked):
    solved = False
    endGame = False
    if (choice == 1):
        prize = spin_the_wheel()
        if (prize != 'BANKRUPT'):
            print(f'The wheel landed on {"${:,}".format(prize)}.')
            balance = pick_consonant(consonants, vowels, toGuess, secretSentence, prize, consonantsPicked, balance)
        else:
            loss = "${:,}".format(balance)
            print("The wheel landed on BANKRUPT.")
            print(f'You lost {loss}!\n')
            balance = 0
    elif (choice == 2):
        balance = buy_vowel(vowels, consonants, toGuess, secretSentence, balance, vowelsPurchased, consonantsPicked)
    elif (choice == 3):
        solved, balance = solve(toGuess, sentence, balance)
    elif (choice == 4):
        balance = 0
        endGame = True
        solved = True
    return balance, endGame, solved


# Spin the whell function for the rewards
def spin_the_wheel():
    result = (500, 500, 500, 500, 550, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 800,
              800, 900, 2500, 'BANKRUPT', 'BANKRUPT')
    # selecting a random result
    prize = result[random.randint(0, 20)]
    return prize


# Ask user for consonant
def pick_consonant(consonants, vowels, toGuess, secretSentence, prize, consonantsPicked, balance):
    keepGoing = True
    if (len(set(consonants)) == 1):
        print("There are no more consonants to choose.")
        keepGoing = False
    else:
        consonant = (str(input("Pick a consonant: "))).lower()
    no_consonants = 0
    while ((consonant.upper() not in consonants) and keepGoing == True):
        if (consonant.upper() in vowels):
            print("Vowels must be purchased.")
        elif (len(consonant) != 1):
            print("Please enter exactly one character.")
        elif (consonant.upper() in consonantsPicked):
            print(f"The letter {consonant.upper()} has already been used.")
        else:
            print(f'The character {consonant} is not a letter.')
        consonant = (str(input("Pick a consonant: "))).lower()
    while (consonant in secretSentence):
        index = secretSentence.index(consonant)
        toGuess[index] = consonant.upper()
        secretSentence[index] = ' '
        no_consonants += 1
    consonantsPicked.append(consonant.upper())
    consonants[consonants.index(consonant.upper())] = ' '
    amountEarned = prize * no_consonants
    if (no_consonants == 1):
        print(f'There is {no_consonants} {consonant.upper()}, which earns you {"${:,}".format(amountEarned)}.\n')
    elif (no_consonants > 1):
        print(f"There are {no_consonants} {consonant.upper()}'s, which earns you {'${:,}'.format(amountEarned)}.\n")
    else:
        print(f"I'm sorry, there are no {consonant.upper()}'s.\n")
    balance = balance + amountEarned
    return balance


# Lets the user buy a vowel
def buy_vowel(vowels, consonants, toGuess, secretSentence, balance, vowelsPurchased, consonantsPicked):
    priceVowel = 275
    no_vowel = 0
    keepGoing = True
    if (balance >= priceVowel):
        vowel = (str(input("Pick a vowel: "))).lower()
        while ((vowel not in secretSentence) and (keepGoing == True)):
            if (vowel.upper() in vowels):
                print(f"I'm sorry, there are no {vowel.upper()}'s.\n")
                vowels[vowels.index(vowel.upper())] = ' '
                balance = balance - priceVowel
                break
            elif ((vowel.upper() in consonants) or (vowel.upper() in consonantsPicked)):
                print("Consonants cannot be purchased.")
            elif (len(vowel) != 1):
                print("Please enter exactly one character.")
            elif (len(set(vowels)) == 1):
                print("There are no more vowels to purchase.")
                keepGoing = False
            elif (vowel.upper() in vowelsPurchased):
                print(f'The letter {vowel.upper()} has already been purchased.')
            else:
                print(f'The character {vowel} is not a letter.')
            vowel = (str(input("Pick a vowel: "))).lower()
        while (vowel in secretSentence):
            if ((vowel.upper() in consonants) or (vowel.upper() in consonantsPicked)):
                print("Consonants cannot be purchased.")
                vowel = (str(input("Pick a vowel: "))).lower()
            else:
                index = secretSentence.index(vowel)
                toGuess[index] = vowel.upper()
                secretSentence[index] = ' '
                no_vowel += 1
        if (no_vowel > 1):
            print(f"There are {no_vowel} {vowel.upper()}'s.\n")
        elif (no_vowel == 1):
            print(f"There is {no_vowel} {vowel.upper()}.\n")

        if (vowel.upper() in vowels):
            index = vowels.index(vowel.upper())
            vowels[index] = ' '
            vowelsPurchased.append(vowel.upper())
        balance = balance - priceVowel
    else:
        print("You need at least $275 to buy a vowel.\n")

    return balance


# Lets the user guess correct answer
def solve(toGuess, sentence, balance):
    print("Enter your solution.")
    print(f'  Clues: {"".join(toGuess)}')
    guess = (str(input("  Guess: "))).lower()
    if (guess == sentence.lower()):
        if (balance < 1000):
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
    while (endGame == False):
        for round in range(1, 5):
            solved = False
            balance = 0
            # calling the list of phrases from the text files
            phrases = load_phrases()
            size = len(phrases)
            # selecting a phrase from the list
            sentence = phrases[random.randint(0, size - 1)]
            toGuess = []
            secretSentence = []
            # defining vowels and consonants
            vowels = ["A", "E", "I", "O", "U"]
            consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',
                          'Y', 'Z']
            vowelsPurchased = []
            consonantsPicked = []
            balance = 0
            for letter in sentence:
                secretSentence.append(letter.lower())
                if (letter == '-' or letter == '&' or letter == "'"):
                    toGuess.append(letter)
                elif (letter != ' '):
                    toGuess.append('_')
                else:
                    toGuess.append(' ')

            # One round of the game
            while (solved == False):
                display(vowels, consonants, round, toGuess, balance)
                choice = getChoice()
                balance, endGame, solved = action(choice, balance, balanceTotal, vowels, consonants, toGuess,
                                                  secretSentence, sentence, vowelsPurchased, consonantsPicked)

            balanceTotal = balanceTotal + balance
            balanceDisplay = "${:,}".format(balance)
            print(f"\nYou earned {balanceDisplay} this round.\n")

            # Check if the games still has rounds left
            if (endGame == True):
                break
            if (round == 4):
                endGame = True
    # displaying the final results
    print("Thanks for playing!")
    balanceDisplay = "${:,}".format(balanceTotal)
    print(f'You earned a total of {balanceDisplay}.')


if __name__ == '__main__':
    main()