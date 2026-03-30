import random

lowest_num = 0
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f"Guess a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"Please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print(f"CORRECT! The answer was {answer}.")
            print(f"You guessed it in {guesses} guesses.")
            is_running = False  # Stop the game
    else:
        print("Invalid guess, try again.")

print("Thanks for playing!")