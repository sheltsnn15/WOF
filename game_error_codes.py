class GameErrorCodes:
    LETTER_ALREADY_GUESSED = 1
    ONLY_ONE_CHARACTER = 2
    INVALID_INPUT = 3
    PLAY_AGAIN = 4

    err_messages = {
        LETTER_ALREADY_GUESSED: "You already guessed that letter",
        ONLY_ONE_CHARACTER: "Please enter exactly one character.",
        INVALID_INPUT: "Invalid input",
        PLAY_AGAIN: "Would you like to play again? [Y/N]",
    }

