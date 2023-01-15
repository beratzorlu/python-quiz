def display_next_question(question_number):
    question = QUIZ_QUESTIONS[question_number]
    print(question["questions"])
    print(question["choices"])

def get_user_answer():
    is_user_input_invalid = True
    while is_user_input_invalid:
        user_input = input("Please enter a value between 1-4...")
        is_user_input_invalid != validate_user_input(user_input)
        if (is_user_input_invalid()):
            print("Invalid value. Please enter a value between 1-4...")
    return user_input



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
