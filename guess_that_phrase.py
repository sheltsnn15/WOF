from game_error_codes import GameErrorCodes
import random as random

from guess_that_phrase_dao import Guess_That_Phrase_DAO


class Guess_That_Phrase:

    def __init__(self):
        self.sentence = ""
        self.letters_picked = []

    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Main display
    def main_display(self, phrase_to_guess):
        phrase = "".join(phrase_to_guess)
        print(f'---------------- Welcome to the Wheel of Fortune! -----------------')
        print(f'     {phrase:^{54}}')
        print()
        print(f'Available Letters:  {"".join(self.LETTERS)}')
        print()

    # Ask user choice
    def get_user_choice(self):
        valid_choice = False
        correct = ['1', '2', '3', '4']
        while not valid_choice:
            print("\nMenu:")
            print("  1 - Guess a letter.")
            print("  2 - Solve the puzzle.")
            print("  3 - Quit the game.")
            choice = str(input("\nEnter the number of your choice: "))
            if choice in correct:
                valid_choice = True
            else:
                print(f"{choice} is an invalid choice.\n")
        return int(choice)

    # User action process method

    def process_user_action(self, choice, phrase_to_guess, loaded_phrase):
        solved = False
        end_game = False
        if choice == 1:
            solved = self.guess_letter(phrase_to_guess, loaded_phrase)
        elif choice == 2:
            solved = self.guess_phrase(phrase_to_guess)
        elif choice == 3:
            end_game = True
            solved = True
        return end_game, solved

    def get_random_phrase(self):
        # calling the list of phrases from the text files
        phrases = Guess_That_Phrase_DAO.get_instance().phrases
        size = len(phrases)
        # select random phrase from the list
        return phrases[random.randint(0, size - 1)]

    # Ask user for a letter
    def guess_letter(self, phrase_to_guess, loaded_phrase):
        letter = (str(input("Pick a letter: "))).lower()
        num_letters = 0
        while letter.upper() not in self.LETTERS:
            if len(letter) != 1:
                print(f"{GameErrorCodes.ONLY_ONE_CHARACTER}")
            elif letter.upper() in self.letters_picked:
                print(f"{GameErrorCodes.LETTER_ALREADY_GUESSED}")
            else:
                print(f"{GameErrorCodes.INVALID_INPUT}")
            letter = (str(input("Pick a letter: "))).lower()
        while letter in loaded_phrase:
            index = loaded_phrase.index(letter)
            phrase_to_guess[index] = letter.upper()
            loaded_phrase[index] = ' '
            num_letters += 1
        self.letters_picked.append(letter.upper())
        self.LETTERS[self.LETTERS.index(letter.upper())] = ' '
        if num_letters == 1:
            print(f'There is {num_letters} {letter.upper()}.\n')
        elif num_letters > 1:
            print(f"There are {num_letters} {letter.upper()}'s.\n")
        else:
            print(f"I'm sorry, there are no {letter.upper()}'s.\n")

    # Lets the user guess correct answer
    def guess_phrase(self, phrase_to_guess):
        print("Enter your solution.")
        print(f'  Clues: {"".join(phrase_to_guess)}')
        guess = (str(input("  Guess: "))).lower()
        if guess == self.sentence.lower():
            print(f"{GameErrorCodes.HAVE_WON}")
            return True
        else:
            print("I'm sorry. Your guess is incorrect:")
            print(self.sentence.upper())
            return False

    def starting_point(self):
        new_game = ""
        # greeting the user
        print("Welcome to GUESS THAT PHRASE!\n")
        while new_game != "N":
            end_game = False
            while not end_game:
                solved = False

                self.sentence = self.get_random_phrase()

                phrase_to_guess = []
                loaded_phrase = []

                for letter in self.sentence:
                    loaded_phrase.append(letter.lower())
                    if letter == '-' or letter == '&' or letter == "'":
                        phrase_to_guess.append(letter)
                    elif letter != ' ':
                        phrase_to_guess.append('_')
                    else:
                        phrase_to_guess.append(' ')

                while not solved:
                    self.main_display(phrase_to_guess)
                    choice = self.get_user_choice()
                    solved, end_game = self.process_user_action(
                        choice, phrase_to_guess, loaded_phrase)

                    check_solution = ""
                    check_solution = check_solution.join(phrase_to_guess)
                    if self.sentence.upper() == check_solution:
                        print(f"{GameErrorCodes.HAVE_WON}")
                        end_game = True
                    if end_game:
                        break

        print("Well done! Goodbye.!")


if __name__ == '__main__':
    gtf = Guess_That_Phrase()
    gtf.starting_point()
