"""
Import libraries essential to the function of this application.
"""
import database as db
import time
from time import sleep
from questions import QUIZ_QUESTIONS
from questions import QUIZ_CHOICES
from colours import QuizColours as C


def welcome_logo():
    """
    Display game logo on the terminal.
    """
    print(' ')
    print(C.Y + 'Presenting:')
    print(' ')
    print(C.R + ' _____           _                     ___             _    ')
    print(C.R + '/  ___|         | |                   |_  |           | |   ')
    print(C.G + '\ `--. _   _ ___| |_ ___ _ __ ___       | |_   _ _ __ | | __')
    print(C.G + " `--. \ | | / __| __/ _ \ '_ ` _ \      | | | | | '_ \| |/ /")
    print(C.G + '/\__/ / |_| \__ \ ||  __/ | | | | | /\__/ / |_| | | | |   < ')
    print(C.G + '\____/ \__, |___/\__\___|_| |_| |_| \____/ \__,_|_| |_|_|\_\ ')
    print(C.R + '         _/ |                                               ')
    print(C.R + '        |___/                                               ')
    print(' ')
    print(C.Y + '                                          By Berat Zorlu')
    print(' ')
    time.sleep(1.3)


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
    print(C.Y + 'Please choose *ONE* choice from (A, B, C, D)\n')
    print(C.R + 'Disclaimer: ' + C.Y + 
          'Entered input can only be a choice letter.\n')
    for key in QUIZ_QUESTIONS:
        print('---')
        print(key)
        for choice in QUIZ_CHOICES[current_question_num-1]:
            print(choice)
        answer_attempt = input(C.G + "Enter your answer here:\n")
        answer_attempt = answer_attempt.upper()
        answer_attempts.append(answer_attempt)
        user_guesses_correct += validate_user_input(QUIZ_QUESTIONS.get(key),
            answer_attempt)
        current_question_num += 1

    display_user_score(user_guesses_correct, answer_attempts)


def validate_user_input(correct_answer, answer_attempt):
    """
    Compare the correct answer with user's answer attempt.
    Display feedback depending on the correctness of user's answer.
    """
    # Error handling issue 17.01.2023 ~17:00
    if correct_answer == answer_attempt:
        print(' ')
        print(C.G + "Your answer is correct!\n")
        return 1
    if correct_answer != answer_attempt:
        print(' ')
        print(C.R + "Incorrect answer.\n")
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
    print('---')
    print(C.Y + "Quiz Results")
    print('---')
    print(C.G + "Answers: \n", end=" ")
    sheet_list = []
    for ind in QUIZ_QUESTIONS:
        print(QUIZ_QUESTIONS.get(ind), end=" ")
    print(' ')
    print("Your choices: \n", end=" ")
    for ind in answer_attempts:
        print(ind, end=" ")
    print(' ')
    final_score_perc = int((user_guesses_correct/len(QUIZ_QUESTIONS))*100)
    final_score = (user_guesses_correct * 100)
    sheet_list.append(final_score)
    sheet_list.append(final_score_perc)
    db.update_worksheet(sheet_list, 'user')
    print(f'Your final score is: {final_score}\n')
    print(f'You have performed with an accuracy of "{str(final_score_perc)}%"\n')


def replay_quiz():
    """
    Ask user if they wish to play the quiz again.
    Depending on their choice either;
        -If yes, start the quiz again.
        -If no, terminate the application.
    """
    replay = input(C.Y + 'Would you like to try again? (Y/N)\n')
    replay = replay.upper()
    if replay == "Y":
        print(C.B + 'Restarting application...\n')
        time.sleep(1)
        welcome_logo()
        run_new_quiz()
        return True
    elif replay == "N":
        print(' ')
        print(C.B + 'Terminating application...\n')
        time.sleep(1)
        print(C.Y + 'Thank you for playing.\n')
        print(C.Y + 'Copyright Berat Zorlu - 2023')
        return False
    elif input not in {replay == "Y", replay == "N"}:
        print(C.R + "Invalid input submitted. Please enter 'Y' or 'N'")
        time.sleep(1)
        replay_quiz()
    else:
        return True

    
def main():
    """
    Execute all fundamental program functions.
    """
    welcome_logo()
    run_new_quiz()

    while replay_quiz():
        run_new_quiz()


main()
