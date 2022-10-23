class GameErrorCodes:
    SUCCESS = 1
    INVALID_LETTER_LENGTH = 2
    LETTER_NOT_ALPHA = 3
    INVALID_GUESS_TYPE = 4
    LETTER_ALREADY_GUESSED = 5
    NOT_YES_NO = 6

    err_messages = {
        INVALID_LETTER_LENGTH: "Letter must have exactly 1 character",
        LETTER_NOT_ALPHA: "Letter must be an alphabetic character",
        INVALID_GUESS_TYPE: "The guess type must be either 1 (letter) or 2 (word)",
        LETTER_ALREADY_GUESSED: "You already guessed that letter",
        NOT_YES_NO: "That wasn't 'yes' or 'no'"
    }

