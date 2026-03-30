import random

options = ("Rock", "Paper", "Scissors")
rounds = 0
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors! Best of 3 rounds.\n")

while rounds < 3:
    user = None  # Reset user choice each round
    computer = random.choice(options)  # New computer choice each round

    while user not in options:
        user = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

    print(f"Player: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You Win this round!")
        user_score += 1
    else:
        print("You Lose this round!")
        computer_score += 1

    rounds += 1
    print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

# ------------------------------------------------------------
# Final Result
# ------------------------------------------------------------
if user_score > computer_score:
    print(f"You Won by {user_score - computer_score} point(s)! Final Score: You {user_score} - Computer {computer_score}")
elif user_score == computer_score:
    print(f"It's a Tie! Final Score: You {user_score} - Computer {computer_score}")
else:
    print(f"You Lost by {computer_score - user_score} point(s)! Final Score: You {user_score} - Computer {computer_score}")
