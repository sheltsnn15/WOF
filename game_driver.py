import random as random
from game_error_codes import GameErrorCodes
from game_results import GameResults
from hangman import Hangman


def _get_user_input(prompt, validator=lambda x: GameErrorCodes.SUCCESS):
    while True:
        user_input = input(prompt).lower()
        is_valid = validator(user_input)
        if is_valid is not GameErrorCodes.SUCCESS:
            print(GameErrorCodes.err_messages[is_valid])
        else:
            return user_input


def repeat():
    def is_yes_no(yn):
        if yn[0].lower() in ["y", "n"]: return GameErrorCodes.SUCCESS
        return GameErrorCodes.NOT_YES_NO

    return _get_user_input("Play again (Y/N)?", is_yes_no)


def get_guess_type():
    return _get_user_input("Enter 1 to guess a letter, or 2 to guess the word")


def get_word_guess():
    return _get_user_input("What word would you like to guess? ")


def _get_category_prompt(header, options, underline="="):
    prompt = "\n".join([header, underline * len(header)])
    options = "\n".join(["\t".format(category) for category in options])
    return "\n".join([prompt, options])

def random_phrase():
    line_num = 0
    selected_line = ''
    with open("phrases.txt", "r") as f:
        while 1:
            line = f.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()

class HangmanDriver:

    def __init__(self):
        self.phrase = random_phrase
        self.game = None

    def display_status(self):
        print("Current status: {}".format(self.game.display_letters))
        print()

    def loop(self):
        guess_result = None
        while True:
            word = self.get_word_to_guess()
            self.game = Hangman(word)
            while True:
                self.display_status()
                guess_type = get_guess_type()
                if guess_type == 1:
                    letter = self.get_letter_guess()
                    guess_result = self.game.guess_letter(letter)
                elif guess_type == 2:
                    word = get_word_guess()
                    guess_result = self.game.guess_word(word)

                print(GameResults.result_messages[guess_result])
                if guess_result == GameResults.GAME_WON:
                    break
            play_again = repeat()
            if play_again[0].lower() == "n": break

    def get_word_to_guess(self):
        prompt = _get_category_prompt("Categories:", self.phrase)

        def is_valid_category(category):
            if category not in self.phrase: return GameErrorCodes.UNKNOWN_CATEGORY
            return GameErrorCodes.SUCCESS

        return random.choice(self.phrase[_get_user_input(prompt, is_valid_category)])

    def get_letter_guess(self):
        def is_valid_letter(letter):
            if len(letter) != 1: return GameErrorCodes.INVALID_LETTER_LENGTH
            if not letter.isalpha(): return GameErrorCodes.LETTER_NOT_ALPHA
            if self.game.letter_already_guessed(letter): return GameErrorCodes.LETTER_ALREADY_GUESSED

            return GameErrorCodes.SUCCESS

        return _get_user_input("What letter would you like to guess? ",
                                    is_valid_letter)


if __name__ == '__main__':
    print(random_phrase())
    HangmanDriver().loop()