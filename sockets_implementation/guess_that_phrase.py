import random as random

from error_codes import GameErrorCodes
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
        # keep track of letters guessed by user
        self.letters_already_picked = []
        # this will act as a "control" list variable,
        # so we don't keep track of letters guessed by the user,
        # compared to phrase we loaded from the txt file
        self.loaded_phrase = []
        # keep track of letters guessed and add them to the same index as the characters in the phrase
        self.phrase_to_guess = []
        self.sentence = get_random_phrase()
        self.hide_phrase()

    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Main display
    def main_display(self):
        phrase = "".join(self.phrase_to_guess)
        print(f'---------------- Current Game Status -----------------\n'
              f'{phrase:^{54}}\n\n'
              f'Available Letters:  {"".join(self.LETTERS)}\n\n')

    # Ask user choice

    # User action process method

    def process_user_action(self, choice):
        if choice == 1:
            letter = str(input("Pick a letter: ")).lower()
            self.guess_letter(letter)
        elif choice == 2:
            guess = (str(input("  Guess: "))).lower()
            self.guess_phrase(guess)
        elif choice == 3:
            print("Goodbye.!")
            exit()

    def track_guessed_letters(self, letter):
        num_letters = 0
        # append correctly guessed letters phrase to guess list
        while letter in self.loaded_phrase:
            # get the index of the correctly guessed letter from loaded phrase
            index = self.loaded_phrase.index(letter)
            # replace underscore with the letter
            self.phrase_to_guess[index] = letter.upper()
            # replace letter found loaded phrase list,
            # so we don't have to find the same letter in the next user guess
            self.loaded_phrase[index] = ' '
            # show the user amount of times the letter guessed is in the phrase
            num_letters += 1
        # append the letter already guessed to the letters_already_picked list variable
        self.letters_already_picked.append(letter.upper())
        # remove letters already picked from the LETTERS list variable,
        # just to show user what letter is available
        self.LETTERS[self.LETTERS.index(letter.upper())] = ' '
        if num_letters == 1:
            print(f'There is {num_letters} {letter.upper()}.\n')
        elif num_letters > 1:
            print(f"There are {num_letters} {letter.upper()}'s.\n")
        else:
            print(f"I'm sorry, there are no {letter.upper()}'s.\n")

    # Ask user for a letter
    def guess_letter(self, letter):
        while letter.upper() not in self.LETTERS:
            if len(letter) != 1:
                print(f"{GameErrorCodes.ONLY_ONE_CHARACTER}")
            elif letter.upper() in self.letters_already_picked:
                print(f"{GameErrorCodes.LETTER_ALREADY_GUESSED}")
            else:
                print(f"{GameErrorCodes.INVALID_INPUT}")
            letter = (str(input("Pick a letter: "))).lower()

        self.track_guessed_letters(letter)

    # Lets the user guess correct answer
    def guess_phrase(self, guess):
        print("Enter your solution.")
        print(f'  Clues: {"".join(self.phrase_to_guess)}')
        if guess.upper() == self.sentence.upper():
            self.phrase_to_guess = guess.upper()
        else:
            print("I'm sorry. Your guess is incorrect:")
            print(self.sentence.upper())

    def has_won(self):
        check_solution = ""
        check_solution = check_solution.join(self.phrase_to_guess)
        if check_solution.upper() == self.sentence.upper():
            print(f"{GameErrorCodes.HAVE_WON}")
        return self.sentence.upper() == check_solution.upper()

    def hide_phrase(self):
        # replace letters in phrase with dashes
        for letter in self.sentence:
            self.loaded_phrase.append(letter.lower())
            if letter == '-' or letter == '&' or letter == "'" or letter == ",":
                self.phrase_to_guess.append(letter)
            elif letter != ' ':
                self.phrase_to_guess.append('_')
            else:
                self.phrase_to_guess.append(' ')

    def play_game(self):
        # greeting the user
        print("Welcome to GUESS THAT PHRASE!\n")
        end_game = False
        while not end_game:

            self.main_display()
            choice = get_user_choice()
            self.process_user_action(
                choice)

            end_game = self.has_won()
            if end_game:
                break


if __name__ == '__main__':
    gtf = GuessThatPhrase()
    gtf.play_game()
