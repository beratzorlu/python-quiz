"""
Import questions and choices to be utilized by the program.
Execute the quiz functionality
Push user data to databases
"""
from pprint import pprint
from questions import QUIZ_QUESTIONS
from questions import QUIZ_CHOICES



def run_new_quiz():
    answer_attempts = []
    user_guesses_correct = 0
    current_question_num = 1
    print('Please choose *ONE* choice from (A, B, C, D)\n')
    print('Disclaimer: Entered input can only be a choice letter.\n')
    for key in QUIZ_QUESTIONS:
        print('--')
        print(key)
        for choice in QUIZ_CHOICES[current_question_num-1]:
            print(choice)
        answer_attempt = input("Enter your answer here:\n")
        answer_attempt = answer_attempt.upper()
        answer_attempts.append(answer_attempt)
        current_question_num += 1



def main():
    """
    Execute all fundamental program functions.
    """
    run_new_quiz()
    # validate_user_input()
    # display_user_score()
    # replay_quiz()


main()



























"""
def display_next_question(question_number):
    question = QUIZ_QUESTIONS[question_number]
    print(question["question"])
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
    while question_number < len(QUIZ_QUESTIONS):
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
"""