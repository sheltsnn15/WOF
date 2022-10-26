class GameResults:
    GAME_WON = 1
    ALREADY_GUESSED = 2
    OUT_OF_TRIES = 3
    LETTER_NOT_FOUND = 4
    LETTER_FOUND = 5
    WRONG_WORD = 6

    result_messages = {
        GAME_WON: "You won the game!",
        ALREADY_GUESSED: "You've guessed that letter before!",
        OUT_OF_TRIES: "You ran out of tries - you lose!",
        LETTER_NOT_FOUND: "This letter wasn't in the word - try again!",
        LETTER_FOUND: "You found a letter!",
        WRONG_WORD: "That isn't the right word!"
    }