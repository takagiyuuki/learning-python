import tk
import Interface

current_number = 0
first_term = 0
second_term = 0
result = 0


def do_plus():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0


def do_eq():
    global second_term
