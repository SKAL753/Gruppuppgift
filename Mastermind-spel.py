import random
def validate_input(user_input): 
        user_input_lst = list(user_input)
        if len(user_input_lst) == 4:
            for item in user_input_lst:
                if not item.isdigit():
                    return False
                if int(item) > 6 or int(item) < 1:
                    return False
            return True
        return False
        
def get_input(line):
    while True:
        user_input = input(line)
        user_input = user_input.replace(" ", "")
        if validate_input(user_input):
            lst_user_input = list(user_input)
            lst_user_input = [int(number) for number in lst_user_input]
            return lst_user_input

def write_output(guesses, feedback):
    print(f"{"Försök":<20}{"Gissning":<20}{"Feedback"}\n{"-"*50}")
    for i in range(12, 0, -1):
        if guesses and feedback and i <= len(guesses):
            guess = "".join(map(str, guesses[i-1]))
            print(f"{i:>2}{'.':<20}{guess:<20}{" ".join(feedback[i-1])}\n")
        else:
            print(f"{i:>2}{".":<20}{"":<20}{""}\n")

def write_welcome():
    print("Välkommen till Mastermind!")
    print("Du ska gissa en fyrsiffrig kod med siffror mellan 1 och 6.")
    print("Du har 12 försök på dig att gissa koden.")
    print("Efter varje gissning får du feedback i form av antal rätta siffror på rätt plats ( ✔ ) och antal rätta siffror på fel plats ( ☐ ).")
    print("Lycka till!")

def write_win_message():
    print("Grattis du gissade rätt!")

def write_loss_message():
    print("Du förlorade, bättre lycka nästa gång!")

def create_number():
    number = []
    for i in range(4):
        number.append(random.randint(1,6))
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
    correct_number = create_number()
    print(correct_number)
    while amount_guesses < 12:
        user_guess = get_input("Skriv in din gissning\n> ")
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

