"""
Import libraries essential to the function of this application.
"""
from pprint import pprint
from questions import QUIZ_QUESTIONS
from questions import QUIZ_CHOICES


def run_new_quiz():
    """
    Display input information to the player.
    Iterate through the questions list.
    Iterate through the choices list.
    Ask for question answer attempt from the user.
    Append the chosen answer of the user to answer_attempts list.
    Validate user input.
    Increment question number by 1.
    Display user score after last question.

    """
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
        user_guesses_correct += validate_user_input(QUIZ_QUESTIONS.get(key), answer_attempt)
        current_question_num += 1

    display_user_score(user_guesses_correct, answer_attempts)


def validate_user_input(correct_answer, answer_attempt):
    """ 
    Compare the correct answer with user's answer attempt.
    Display feedback depending on the correctness of user's answer.
    """
    if correct_answer == answer_attempt:
        print("Your answer is correct!\n")
        return 1
    print("Incorrect answer.\n")
    return 0


def display_user_score(user_guesses_correct, answer_attempts):
    """
    Print informative text about quiz completion and score calculation.
    Iterate through the questions list to extract and display correct answers.
    Iterate through answer_attempts to display user's answer attempt history.
    Calculate a percentage value to display user's overall accuracy.
    """
    print(' ')
    print('--\n')
    print('You have completed the quiz, calculating results...\n')
    print('--')
    print("Results")
    print('--')
    print("Answers: ", end=" ")
    for ind in QUIZ_QUESTIONS:
        print(QUIZ_QUESTIONS.get(ind), end=" ")
    print(' ')
    print("Your choices: ", end=" ")
    for ind in answer_attempts:
        print(ind, end=" ")
    print(' ')
    final_score = int((user_guesses_correct/len(QUIZ_QUESTIONS))*100)
    print(f'You have performed with an accuracy of "{str(final_score)}%"')


def replay_quiz():
    """
    Ask user if they wish to play the quiz again.
    Depending on their choice either;
        -If yes, start the quiz again.
        -If no, terminate the application.
    """
    replay = input('Would you like to try again? (Y/N)\n')
    replay = replay.upper()
    if replay == "Y":
        return True
    return False

   
def main():
    """
    Execute all fundamental program functions.
    """
    run_new_quiz()
    replay_quiz()


while replay_quiz():
    run_new_quiz()
    print('Ending quiz and saving user data...')
    print('Terminating application...')
    print('Thank you for playing.')

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