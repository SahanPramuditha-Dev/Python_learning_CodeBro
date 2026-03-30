# Tuple containing all quiz questions
questions = ("How many elements are in the periodic table ?",
             "which animal lays the largest eggs ?",
             "What is the most abundant gas in the earth's atmosphere ?",
             "How many bones are in the human body",
             "Which planet in our solar system is the hottest ?"
             )

# Tuple of tuples — each inner tuple holds the answer choices for a question
options = (("A. 118","B. 119","C. 120","D. 121"),
          ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Carbon dioxide","D. Hydrogen"),
          ("A. 206","B. 207","C. 208","D. 209"),
          ("A. Venus","B. Mars","C. Jupiter","D. Saturn")
          )

# Tuple storing the correct answer letter for each question
answers = ("A","D","A","A","A")

# Empty list to store the user's guesses
guesses = []

# Variable to keep track of correct answers
score = 0

# Index number to track which question we are on
question_num = 0


# Loop through each question in the questions tuple
for question in questions:
    print("-----------------------")
    print(question)  # Display the current question

    # Display the corresponding answer options
    for option in options[question_num]:
        print(option)

    # Ask the user for their answer and convert it to uppercase
    guess = input("Enter (A, B, C, D): ").upper()

    # Store the user's guess in the guesses list
    guesses.append(guess)

    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1  # Increase score if correct
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    print("-----------------------")

    # Move to the next question index
    question_num += 1


# Display results header
print("-----------------------")
print("       RESULTS        ")
print("-----------------------")

# Reset question index to display results from the beginning
question_num = 0

# Loop through answers to show summary of performance
for answer in answers:
    print(f"Question: {questions[question_num]}")
    print(f"Your Answer: {guesses[question_num]}")
    print(f"Correct Answer: {answers[question_num]}")
    question_num += 1

# Calculate and display final percentage score
score_percent = int((score / len(questions)) * 100)
print(f"\nYour final score is: {score_percent}%")
