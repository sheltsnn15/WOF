from game_error_codes import GameErrorCodes
import random as random

from guess_that_phrase_dao import Guess_That_Phrase_DAO

VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']


class Hangman:
    def __init__(self, vowe):
        self.vowels_picked = []
        self.consonants_picked = []
        # calling the list of phrases from the text files


# Main display
def main_display(phrase_to_guess):
    phrase = "".join(phrase_to_guess)
    print(f'---------------- Guess That Phrase Game -----------------')
    print(f'  {phrase:^{54}} ')
    print("                                                          ")
    print(f'     {"".join(VOWELS)}        {"".join(CONSONANTS)}          ')
    print(f'                                                         ')


# Ask user choice
def get_user_choice():
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


# User action process method
def process_user_action(choice, phrase_to_guess, loaded_phrase, sentence, vowels_picked,
                        consonants_picked):
    solved = False
    end_game = False
    if choice == 1:
        guess_consonant(phrase_to_guess, loaded_phrase, consonants_picked)
    elif choice == 2:
        guess_vowel(phrase_to_guess, loaded_phrase, vowels_picked, consonants_picked)
    elif choice == 3:
        solved = guess_phrase(phrase_to_guess, sentence)
    elif choice == 4:
        end_game = True
        solved = True
    return end_game, solved


# Ask user for consonant
def guess_consonant(phrase_to_guess, loaded_phrase, consonants_picked):
    carry_on = True
    if len(set(CONSONANTS)) == 1:
        print("There are no more consonants to choose.")
        carry_on = False
    else:
        consonant = (str(input("Pick a consonant: "))).lower()
    num_consonants = 0
    while (consonant.upper() not in CONSONANTS) and carry_on == True:
        if consonant.upper() in VOWELS:
            print("Vowels cannot be picked.")
        elif len(consonant) != 1:
            print(f"{GameErrorCodes.ONLY_ONE_CHARACTER}")
        elif consonant.upper() in consonants_picked:
            print(f"{GameErrorCodes.LETTER_ALREADY_GUESSED}")
        else:
            print(f"{GameErrorCodes.INVALID_INPUT}")
        consonant = (str(input("Pick a consonant: "))).lower()
    while consonant in loaded_phrase:
        index = loaded_phrase.index(consonant)
        phrase_to_guess[index] = consonant.upper()
        loaded_phrase[index] = ' '
        num_consonants += 1
    consonants_picked.append(consonant.upper())
    CONSONANTS[CONSONANTS.index(consonant.upper())] = ' '
    if num_consonants == 1:
        print(f'There is {num_consonants} {consonant.upper()}.\n')
    elif num_consonants > 1:
        print(f"There are {num_consonants} {consonant.upper()}'s.\n")
    else:
        print(f"I'm sorry, there are no {consonant.upper()}'s.\n")


# Lets the user buy a vowel
def guess_vowel(phrase_to_guess, loaded_phrase, vowels_picked, consonants_picked):
    num_vowel = 0
    carry_on = True
    vowel = (str(input("Pick a vowel: "))).lower()
    while (vowel not in loaded_phrase) and (carry_on == True):
        if vowel.upper() in VOWELS:
            print(f"I'm sorry, there are no {vowel.upper()}'s.\n")
            VOWELS[VOWELS.index(vowel.upper())] = ' '
            break
        elif (vowel.upper() in CONSONANTS) or (vowel.upper() in consonants_picked):
            print("Consonants cannot be picked.")
        elif len(vowel) != 1:
            print(f"{GameErrorCodes.ONLY_ONE_CHARACTER}")
        elif len(set(VOWELS)) == 1:
            print("There are no more vowels to choose.")
            carry_on = False
        elif vowel.upper() in vowels_picked:
            print(f"{GameErrorCodes.LETTER_ALREADY_GUESSED}")
        else:
            print(f"{GameErrorCodes.INVALID_INPUT}")
        vowel = (str(input("Pick a vowel: "))).lower()
    while vowel in loaded_phrase:
        if (vowel.upper() in CONSONANTS) or (vowel.upper() in consonants_picked):
            print("Consonants cannot be picked.")
            vowel = (str(input("Pick a vowel: "))).lower()
        else:
            index = loaded_phrase.index(vowel)
            phrase_to_guess[index] = vowel.upper()
            loaded_phrase[index] = ' '
            num_vowel += 1
    if num_vowel > 1:
        print(f"There are {num_vowel} {vowel.upper()}'s.\n")
    elif num_vowel == 1:
        print(f"There is {num_vowel} {vowel.upper()}.\n")

    if vowel.upper() in VOWELS:
        index = VOWELS.index(vowel.upper())
        VOWELS[index] = ' '
        vowels_picked.append(vowel.upper())


# Lets the user guess correct answer
def guess_phrase(phrase_to_guess, sentence):
    print("Enter your solution.")
    print(f'  Clues: {"".join(phrase_to_guess)}')
    guess = (str(input("  Guess: "))).lower()
    if guess == sentence.lower():
        print(f"{GameErrorCodes.HAVE_WON}")
        return True
    else:
        print("I'm sorry. Your guess is incorrect:")
        print(sentence.upper())
        return False


def main():
    new_game = ""
    # greeting the user
    print("Welcome to GUESS THAT PHRASE!\n")
    while new_game != "N":
        end_game = False
        while not end_game:
            solved = False
            # calling the list of phrases from the text files
            phrases = Guess_That_Phrase_DAO.get_instance().phrases
            size = len(phrases)
            # select random phrase from the list
            sentence = phrases[random.randint(0, size - 1)]
            phrase_to_guess = []
            loaded_phrase = []
            # defining vowels and consonants

            vowels_picked = []
            consonants_picked = []
            for letter in sentence:
                loaded_phrase.append(letter.lower())
                if letter == '-' or letter == '&' or letter == "'":
                    phrase_to_guess.append(letter)
                elif letter != ' ':
                    phrase_to_guess.append('_')
                else:
                    phrase_to_guess.append(' ')

            while not solved:
                main_display(phrase_to_guess)
                choice = get_user_choice()
                solved, end_game = process_user_action(choice, phrase_to_guess, loaded_phrase,
                                                       sentence, vowels_picked, consonants_picked)

                check_solution = ""
                check_solution = check_solution.join(phrase_to_guess)
                if sentence.upper() == check_solution:
                    print(f"{GameErrorCodes.HAVE_WON}")
                    end_game = True
                if end_game:
                    break

        choices = ['Y', 'y', 'N', 'n']

        valid_input = True
        while valid_input:
            user_input = input(f"{GameErrorCodes.PLAY_AGAIN}: ")
            if user_input.upper() in choices:
                new_game = user_input.upper()
                print(new_game)
                valid_input = False
            else:
                print(f"{GameErrorCodes.INVALID_INPUT}")

    # displaying the final results
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
