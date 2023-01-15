#Quiz

QUESTIONS = ("Question1",  
             "Question2", 
             "Question3", 
             "Question4", 
             "Question5")

CHOICES = (("I. Choice1", "II. Choice2", "III. Choice3", "IV. Choice4"),
           ("I. Choice11", "II. Choice22", "III. Choice33", "IV. Choice44"),
           ("I. Choice111", "II. Choice222", "III. Choice333", "IV. Choice444"),
           ("I. Choice1111", "II. Choice2222", "III. Choice3333", "IV. Choice4444"),
           ("I. Choice11111", "II. Choice22222", "III. Choice33333", "IV. Choice44444"))

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
