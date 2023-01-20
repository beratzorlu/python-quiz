"""
Import libraries essential to the function of this application.
"""
import sys
import os
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


def game_lore():
    """
    Display a series of text relevant to the narrative of the game.
    Space out the text by placing time pauses between each print.
    Add colour to certain parts to add styling.
    Clear screen and prepare the space for the quiz questions.
    """
    print_text_slow('In the dystopian future of 2555...\n')
    time.sleep(1)
    print_text_slow('Mankind has abandoned the pursue of arts.\n')
    time.sleep(1)
    print_text_slow('Our planet continuously degraded...\n')
    time.sleep(1)
    print_text_slow('Industry and society only benefited from technology.\n')
    time.sleep(1)
    print_text_slow('Science became a neccessity for survival.\n')
    time.sleep(1)
    print_text_slow('All other pursuits were shunned by society.\n')
    time.sleep(1)
    print_text_slow('Today, every soul is expected to know science.\n')
    time.sleep(1)
    print_text_slow('Citizens are tested for their fundamental knowledge.\n')
    time.sleep(1)
    print_text_slow('Those who succeed get the privilage to continue their lives.\n')
    time.sleep(1)
    print_text_slow('Those who do not, are discarded as...\n')
    time.sleep(1)
    print(C.R + 'System ' + C.G + 'Junk\n')
    time.sleep(2)
    print('--\n')
    print(C.B + 'Assesment initialization is complete, executing application...\n')
    print('---')
    time.sleep(5)
    clear_screen()


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
    print(C.Y + 'You cannot return to previous questions.')
    print(C.Y + 'You are not allowed to change yours answers.')
    print(C.Y + 'There are 10 question in total.')
    print(C.Y + 'Please choose *ONE* choice from (A, B, C, D)\n')
    print(C.R + 'Disclaimer: ' + C.Y + 
          'Entered input can only be a choice letter.\n')
    for key in QUIZ_QUESTIONS:
        print('---')
        print(key)
        for choice in QUIZ_CHOICES[current_question_num-1]:
            print(choice)
        answer_attempt = input(C.Y + "Enter your answer here:\n")
         # if answer_attempt.strip() == '':
            # print('invalid')
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
    Prompt the user to input a username.
    Validate the username.
    Append acquired data into a list and upload it to the database.
    Calculate a percentage value to display user's overall accuracy.
    """
    sheet_list = []
    username = get_username()
    validate_username(username)
    print(' ')
    print('--\n')
    print(C.B + 'You have completed the quiz, calculating results...\n')
    print('---')
    print(C.Y + "Quiz Results")
    print('---')
    print(C.G + "Answers: \n", end=" ")
    for ind in QUIZ_QUESTIONS:
        print(QUIZ_QUESTIONS.get(ind), end=" ")
    print(' ')
    print(C.G + "Your choices: \n", end=" ")
    for ind in answer_attempts:
        print(ind, end=" ")
    print(' ')
    final_score_perc = int((user_guesses_correct/len(QUIZ_QUESTIONS))*100)
    final_score = (user_guesses_correct * 100)
    list_append(sheet_list, username)
    list_append(sheet_list, final_score)
    list_append(sheet_list, final_score_perc)
    db.update_worksheet(sheet_list, 'user')
    print(f'Displaying performance analysis for "{username}"...\n')
    time.sleep(1)
    print(f'Your final score is: {final_score}\n')
    time.sleep(1)
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
        clear_screen()
        welcome_logo()
        run_new_quiz()
        return True
    elif replay == "N":
        print(' ')
        clear_screen()
        print(C.B + 'Terminating application...\n')
        time.sleep(1)
        print(C.Y + 'Thank you for playing.\n')
        print(C.Y + 'Copyright Berat Zorlu - 2023 for Code Institute PP3')
        return False
    elif input not in {replay == "Y", replay == "N"}:
        print(C.R + "Invalid input submitted. Please enter 'Y' or 'N'")
        time.sleep(1)
        replay_quiz()
    else:
        return True
  

def get_username():
    """
    Display instructive text regarding the expected user input.
    Take user input and assign it to the username variable.
    Pass the variable in validate_username() function.
    If successful, break the while loop and return the username value.
    """
    while True:
        time.sleep(1)
        clear_screen()
        print(C.G + 'You have answered all questions.')
        print(C.G + 'Please provide a username to save your data.\n')
        print(C.B + '1. Your input should consist of 12 characters.\n')
        print(C.B + '2. Input cannot be less than 3 characters.\n')
        print(C.B + '3. Empty values are not accepted.\n')
        username_input = input(C.Y + 'Please provde a username: \n')
        username = username_input

        if validate_username(username):
            print('Valid username entered. Proceessing...\n')
            time.sleep(1)
            clear_screen()
            break
    
    return username


def validate_username(user_input):
    """
    Validate user input by comparing it to various cases.
        -If input is valid, return True.
        -If input is invalid, return False.
    """
    if len(user_input) > 12:
        print(C.R + 'Please do not enter no more than 12 characters.\n')
        return False
    elif user_input == '':
        print(C.R + 'You cannot enter an empty value.\n')
        return False
    elif len(user_input) < 3:
        print(C.R + 'Username cannot be less than 3 characters.\n')
        return False
    elif user_input.strip() == '':
        print(C.R + 'You cannot enter an empty value.\n')
        return False
    else:
        return True


def print_text_slow(str):
    """
    This is to provide a typing animation for the game_lore() function.
    Loop through each character in a string.
    Write each string on the terminal in slow succession.
    """
    for char in str:
        time.sleep(.09)
        sys.stdout.write(char)
        sys.stdout.flush()


def list_append(list, data):
    """
    Take list and data parameters.
    Append data into specified list.
    """
    list.append(data)


def clear_screen():
    """
    Delete all visible text content on console.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Execute all fundamental program functions.
    """
    welcome_logo()
    game_lore()
    run_new_quiz()

    while replay_quiz():
        run_new_quiz()


main()
