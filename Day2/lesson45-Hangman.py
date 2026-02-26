import random

# --------------------------------------------------
# CONSTANT DATA
# --------------------------------------------------

WORDS = (
    "apple", "orange", "banana", "grape",
    "peach", "mango", "strawberry", "watermelon"
)

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

    if len(guess) != 1 or not guess.isalpha(): # 
        print("❌ Invalid input. Enter ONE letter only.")
        return None

    if guess in guessed_letters:
        print("⚠ Letter already guessed.")
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

    while True:
        display_game_state(secret_word, guessed_letters, wrong_guesses)

        # Win condition
        if has_won(secret_word, guessed_letters):
            print("\n🎉 You WIN!")
            print("The word was:", secret_word)
            break

        # Lose condition
        if wrong_guesses >= MAX_WRONG:
            print("\n💀 You LOSE!")
            print("The word was:", secret_word)
            break

        # Get player guess
        guess = get_player_guess(guessed_letters)
        if guess is None:
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print("❌ Wrong guess!")
        else:
            print("✅ Correct guess!")

# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    play_hangman()
