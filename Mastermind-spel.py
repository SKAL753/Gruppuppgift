import random
from enum import Enum

class InputType(Enum):
    GUESS = 1
    DIFFICULTY = 2

def validate_input(user_input, input_type): 
        if input_type == InputType.GUESS:
            user_input_lst = list(user_input)
            if len(user_input_lst) == 4:
                for item in user_input_lst:
                    if not item.isdigit():
                        return False
                    if int(item) > 6 or int(item) < 1:
                        return False
                return True
            return False
        elif input_type == InputType.DIFFICULTY:
            if user_input == "svår" or user_input == "lätt":
                return True
            
def get_input(line, input_type):
    while True:
        user_input = input(line).strip().lower()
        user_input = user_input.replace(" ", "")
        if validate_input(user_input, input_type):
            if input_type == InputType.GUESS:
                return [int(number) for number in user_input]
            return user_input

def write_output(guesses, feedback):
    print(f"{"Försök":<20}{"Gissning":<20}{"Feedback"}\n{"-"*50}")
    for i in range(12, 0, -1):
        if guesses and feedback and i <= len(guesses):
            guess = "".join(map(str, guesses[i-1]))
            print(f"{i:>2}{'.':<20}{guess:<20}{" ".join(feedback[i-1])}\n")
        else:
            print(f"{i:>2}{".":<20}{"":<20}{""}\n")

def write_welcome():
    print("=" * 40)
    print("       Välkommen till Mastermind!")
    print("=" * 40)

    print("\nDu ska gissa en fyrsiffrig kod med siffror mellan 1 och 6.")
    print("Du har 12 försök på dig att gissa koden.")

    print("\nSVÅRIGHETSGRADER")
    print("-" * 20)
    print("Lätt: Koden innehåller inga upprepade siffror.")
    print("Svår: Koden kan innehålla upprepade siffror.")

    print("\nFEEDBACK")
    print("-" * 20)
    print("✔ = Rätt siffra på rätt plats")
    print("☐ = Rätt siffra på fel plats")

    print("\nLycka till!")
    print("=" * 40)

def write_win_message():
    print("Grattis du gissade rätt!")

def write_loss_message():
    print("Du förlorade, bättre lycka nästa gång!")

def create_number(difficulty):
    number = []
    if difficulty == "svår":
        for i in range(4):
            number.append(random.randint(1,6))
    elif difficulty == "lätt":
        number = random.sample(range(1,7), 4)
    return number

def compare_numbers(correct_number, user_guess):
    feedback = []
    remaining = correct_number.copy()

    for i, digit in enumerate(user_guess):
        if digit == correct_number[i]:
            feedback.append("✔")
            remaining.remove(digit)

    for i, digit in enumerate(user_guess):
        if digit != correct_number[i] and digit in remaining:
            feedback.append("☐")
            remaining.remove(digit)

    return feedback

def check_win(correct_number, user_guess):
    return correct_number == user_guess

def main():
    won = False
    amount_guesses = 0
    guesses = []
    all_feedback = []
    write_welcome()
    difficulty = get_input("Välj svårighetsgrad (lätt, svår)\n> ", InputType.DIFFICULTY)
    correct_number = create_number(difficulty)
    while amount_guesses < 12:
        user_guess = get_input("Skriv in din gissning\n> ", InputType.GUESS)
        guesses.append(user_guess)
        amount_guesses += 1
        feedback = compare_numbers(correct_number, user_guess)
        all_feedback.append(feedback)
        write_output(guesses, all_feedback)
        if check_win(correct_number, user_guess):
            won = True
            write_win_message()
            break
        
    if won == False:
        write_loss_message()
        
        
        


if __name__ == "__main__":
    main()

