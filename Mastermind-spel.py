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
            return user_input

def write_output(guesses, feedback):
    print(f"{"Försök":<20}{"Gissning":<20}{"Feedback"}\n{"-"*50}")
    for i in range(12, 0, -1):
        if guesses and feedback and i <= len(guesses):
            print(f"{i:>2}{".":<20}{guesses[i-1]:<20}{feedback[i-1]}\n")
        else:
            print(f"{i:>2}{".":<20}{"":<20}{""}\n")

def write_welcome():
    print("Välkommen till Mastermind!")
    print("Du ska gissa en fyrsiffrig kod med siffror mellan 1 och 6.")
    print("Du har 12 försök på dig att gissa koden.")
    print("Efter varje gissning får du feedback i form av antal rätta siffror på rätt plats ( ✔ ) och antal rätta siffror på fel plats ( ☐ ).")
    print("Lycka till!")

def create_number():
    pass

def compare_numbers():
    pass

guesses = ["1234", "4321", "1111"]
feedback = [" ✔ ", " ☐ ", " ✔ "]
write_output(guesses, feedback)

