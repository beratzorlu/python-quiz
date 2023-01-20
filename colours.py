"""
Colour library for text stylisation for the application.
"""
from colorama import init, Fore

init(autoreset=True)


class QuizColours():
    """
    Class contains shortcuts to various colours used in the application.
    """
    G = Fore.GREEN
    R = Fore.RED
    B = Fore.BLUE
    Y = Fore.YELLOW
