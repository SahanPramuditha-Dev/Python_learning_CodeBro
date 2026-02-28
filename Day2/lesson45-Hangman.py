import random

# --------------------------------------------------
# CONSTANT DATA
# --------------------------------------------------

WORD_HINTS = {
    "apple": "A crunchy red or green fruit.",
    "alone": "By yourself; without others.",
    "bread": "Food used to make a sandwich.",
    "beach": "A sandy place by the ocean.",
    "chair": "Something you sit on.",
    "cloud": "A white fluffy thing in the sky.",
    "dream": "Stories you see while sleeping.",
    "drink": "To swallow a liquid like water.",
    "earth": "The planet we live on.",
    "eagle": "A large bird with sharp eyes.",
    "floor": "What you walk on inside a house.",
    "fruit": "Sweet food like grapes or berries.",
    "glass": "What windows are made of.",
    "green": "The color of grass or leaves.",
    "heart": "It pumps blood through your body.",
    "house": "A building where people live.",
    "lemon": "A sour yellow citrus fruit.",
    "light": "What you turn on when it's dark.",
    "music": "Sounds you listen to for fun.",
    "mouse": "A tiny animal that likes cheese.",
}

WORDS = tuple(WORD_HINTS.keys())

HANGMAN_ART = {
    0: r"""
        +---+
        |   |
            |
            |
            |
            |
        =========""",

    1: r"""
        +---+
        |   |
        O   |
            |
            |
            |
        =========""",

    2: r"""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========""",

    3: r"""
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========""",

    4: r"""
        +---+
        |   |
        O   |
        /|\  |
            |
            |
        =========""",

    5: r"""
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
        =========""",

    6: r"""
        +---+
        |   |
        O   |
        /|\  |
        / \  |
            |
        ========="""
}

MAX_WRONG = 6

# --------------------------------------------------
# FUNCTION: choose a random word
# --------------------------------------------------
def get_random_word():
    return random.choice(WORDS)

# --------------------------------------------------
# FUNCTION: build a hint for the secret word
# --------------------------------------------------
def get_hint(secret_word):
    return WORD_HINTS[secret_word]

# --------------------------------------------------
# FUNCTION: display hangman + word progress
# --------------------------------------------------
def display_game_state(secret_word, guessed_letters, wrong_guesses):
    print(HANGMAN_ART[wrong_guesses])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

# --------------------------------------------------
# FUNCTION: get and validate player input
# --------------------------------------------------
def get_player_guess(guessed_letters):
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter ONE letter only.")
        return None

    if guess in guessed_letters:
        print("Letter already guessed.")
        return None

    return guess

# --------------------------------------------------
# FUNCTION: check win condition
# --------------------------------------------------
def has_won(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

# --------------------------------------------------
# FUNCTION: main game logic
# --------------------------------------------------
def play_hangman():
    secret_word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Hint:", get_hint(secret_word))

    while True:
        display_game_state(secret_word, guessed_letters, wrong_guesses)

        # Win condition
        if has_won(secret_word, guessed_letters):
            print("\nYou WIN!")
            print("The word was:", secret_word)
            break

        # Lose condition
        if wrong_guesses >= MAX_WRONG:
            print("\nYou LOSE!")
            print("The word was:", secret_word)
            break

        # Get player guess
        guess = get_player_guess(guessed_letters)
        if guess is None:
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    play_hangman()
