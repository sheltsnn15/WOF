from game_results import GameResults

class Hangman:

    def __init__(self, word, attempts=7):
        self.word = word
        self.guessed_letters = set()
        self.attempts = attempts

    @property
    def display_letters(self):
        result = ""
        for char in self.word:
            if char in self.guessed_letters:
                result += char
            else:
                result += "_"
        return result

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return GameResults.ALREADY_GUESSED
        self.guessed_letters.add(letter)
        self.attempts -= 1
        if letter not in self.word:
            if self.attempts == 0:
                return GameResults.OUT_OF_TRIES
            return GameResults.LETTER_NOT_FOUND
        if "_" not in self.display_letters:
            return GameResults.GAME_WON
        return GameResults.LETTER_FOUND

    def guess_word(self, word):
        self.attempts -= 1
        if word == self.word:
            return GameResults.GAME_WON
        return GameResults.WRONG_WORD
