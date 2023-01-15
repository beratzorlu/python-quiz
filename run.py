#Quiz

QUIZ_QUESTIONS = [
    {"question": "QUESTION 1",
    "choices": "1. Choice1", "2. Choice2", "3. Choice3", "4. Choice4",
    "answer": 1},
    {"question": "QUESTION 2",
    "choices": "1. Choice1", "2. Choice2", "3. Choice3", "4. Choice4",
    "answer": 1},
    {"question": "QUESTION 3",
    "choices": "1. Choice1", "2. Choice2", "3. Choice3", "4. Choice4",
    "answer": 1},
    {"question": "QUESTION 4",
    "choices": "1. Choice1", "2. Choice2", "3. Choice3", "4. Choice4",
    "answer": 1},
    {"question": "QUESTION 5",
    "choices": "1. Choice1", "2. Choice2", "3. Choice3", "4. Choice4",
    "answer": 1},
]

quiz_answers = ("I", "I", "I", "I", "I")
user_guesses = []
user_score = 0
question_number = 0

for question in QUESTIONS:
    print("|||||||||||||||||||||||||||||")
    print(question)
    for choice in CHOICES[question_number]:
        print(choice)

    user_guess = input("Input correct answer: ").upper()
    user_guesses.append(user_guess)

    if user_guess == quiz_answers[question_number]:
        user_score += 1
        print("Correct. Proceed to the next question...")
    else:
        print("Incorrect. Focus!")
        print(f"The correct answer was '{quiz_answers[question_number]}'")
    
    question_number += 1

#Results

print("Here are the answers: ", end="")
for quiz_answer in quiz_answers:
    print(quiz_answer, end=" ") 
print()

print("These were your guesses: ", end="")
for user_guess in user_guesses:
    print(user_guess, end=" ")
print()

#User Score

user_score = user_score
score_percentage = int(user_score / len(QUESTIONS) * 100)
print(f"Your final score is {user_score}. You have answered {score_percentage}% of the questions correctly.")
