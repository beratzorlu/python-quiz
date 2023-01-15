from questions import QUIZ_QUESTIONS


def display_next_question(question_number):
    question = QUIZ_QUESTIONS[question_number]
    print(question["questions"])
    print(question["choices"])


def get_user_answer():
    is_user_input_invalid = True
    while is_user_input_invalid:
        user_input = input("Please enter a value between 1-4...")
        is_user_input_invalid != validate_user_input(user_input)
        if is_user_input_invalid:
            print("Invalid value. Please enter a value between 1-4...")
    return user_input


def validate_user_input(user_input):
    return user_input and user_input.isnumeric() and int(user_input) >= 1 and int(user_input) <= 4


def check_user_answer(user_input, question_number):
    question = QUIZ_QUESTIONS[question_number]
    return question["answer"] == user_input


def display_final_score(user_score):
    score_percentage = int(user_score / len(QUIZ_QUESTIONS) * 100)
    print(f"Your final score is {user_score}. You have answered {score_percentage}% of the questions correctly.")
    return score_percentage


def update_score_to_gspread(score, score_percentage):
    pass


def main():
    question_number = 0
    score = 0
    while question_number < QUIZ_QUESTIONS.length:
        display_next_question(question_number)
        user_input == get_user_answer()
        is_correct = check_user_answer(user_input, question_number)
        if is_correct:
            score += 100
        question_number += 1
    score_percentage = display_final_score(score)
    update_score_to_gspread(score, score_percentage)


if __name__ == '__main__':
    main()