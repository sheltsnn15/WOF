from error_codes import GameErrorCodes
import random as random

from guess_that_phrase_dao import Guess_That_Phrase_DAO


def get_user_choice():
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


def get_random_phrase():
    # calling the list of phrases from the text files
    phrases = Guess_That_Phrase_DAO.get_instance().phrases
    size = len(phrases)
    # select random phrase from the list
    return phrases[random.randint(0, size - 1)]


class GuessThatPhrase:

    def __init__(self):
        self.sentence = ""
        self.letters_picked = []
        self.loaded_phrase = []
        self.phrase_to_guess = []

    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Main display
    def main_display(self):
        phrase = "".join(self.phrase_to_guess)
        print(f'---------------- Welcome to the Wheel of Fortune! -----------------')
        print(f'     {phrase:^{54}}')
        print()
        print(f'Available Letters:  {"".join(self.LETTERS)}')
        print()

    # Ask user choice

    # User action process method

    def process_user_action(self, choice):
        solved = False
        end_game = False
        if choice == 1:
            letter = str(input("Pick a letter: ")).lower()
            solved = self.guess_letter(letter)
        elif choice == 2:
            solved = self.guess_phrase()
        elif choice == 3:
            end_game = True
            solved = True
        return end_game, solved

    # Ask user for a letter
    def guess_letter(self, letter):
        num_letters = 0
        while letter.upper() not in self.LETTERS:
            if len(letter) != 1:
                print(f"{GameErrorCodes.ONLY_ONE_CHARACTER}")
            elif letter.upper() in self.letters_picked:
                print(f"{GameErrorCodes.LETTER_ALREADY_GUESSED}")
            else:
                print(f"{GameErrorCodes.INVALID_INPUT}")
            letter = (str(input("Pick a letter: "))).lower()
        while letter in self.loaded_phrase:
            index = self.loaded_phrase.index(letter)
            self.phrase_to_guess[index] = letter.upper()
            self.loaded_phrase[index] = ' '
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
    def guess_phrase(self):
        print("Enter your solution.")
        print(f'  Clues: {"".join(self.phrase_to_guess)}')
        guess = (str(input("  Guess: "))).lower()
        if guess == self.sentence.lower():
            print(f"{GameErrorCodes.HAVE_WON}")
            return True
        else:
            print("I'm sorry. Your guess is incorrect:")
            print(self.sentence.upper())
            return False

    def starting_point(self):
        # greeting the user
        print("Welcome to GUESS THAT PHRASE!\n")
        end_game = False
        while not end_game:
            solved = False

            self.sentence = get_random_phrase()

            for letter in self.sentence:
                self.loaded_phrase.append(letter.lower())
                if letter == '-' or letter == '&' or letter == "'":
                    self.phrase_to_guess.append(letter)
                elif letter != ' ':
                    self.phrase_to_guess.append('_')
                else:
                    self.phrase_to_guess.append(' ')

            while not solved:
                self.main_display()
                choice = get_user_choice()
                solved, end_game = self.process_user_action(
                    choice)

                check_solution = ""
                check_solution = check_solution.join(self.phrase_to_guess)
                if self.sentence.upper() == check_solution:
                    print(f"{GameErrorCodes.HAVE_WON}")
                    end_game = True
                if end_game:
                    break

        print("Goodbye.!")


if __name__ == '__main__':
    gtf = GuessThatPhrase()
    gtf.starting_point()
