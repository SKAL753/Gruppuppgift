import random
from enum import Enum

class InputType(Enum): #Enum används för att tydligare visa vad som menas med tex input_type == 1, det blir tydligare om man istället skriver InputType.Guess för då ser man att man kollar om input_type är guess typen. 
    GUESS = 1
    DIFFICULTY = 2

def validate_input(user_input: str, input_type: InputType) -> bool: 
    '''
    Den tar in användarens gissning och input typen och veriferar att inputen är giltig. För gissnings typen gör den först om användarens input till
    en lista och kollar sedan om listan innehåller 4 tecken. Om den gör det kollar den sedan för varje tecken i användarens gissning om det är en siffra
    och sedan om det är en siffra om siffran inte är större än 6 eller mindre än 1 om användarens gissning klarar alla de krav returnerar den True
    eftersom inputen var giltig. För svårighetsgrad typen kollar den bara om användarens input är svår eller lätt om returnerar i det fallet True annars False'''
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
    return False
            
def get_input(line: str, input_type: InputType) -> str | list[int]:
    '''
    Den tar in en fråga, line, och input typen, antingen gissning eller svårighetsgrad. Den använder sig av validate_input för att verifiera
    att inputen från användaren är giltig, om den är giltig returnerar den användarens svar. Den tar in användarens input och tar bort alla mellanrum
    i början eller slutet av strängen och gör alla bokstäver små. Den tar sedan bort alla mellanslag i strängen och går vidare till att validera inputen.
    Om inputen är korrekt returnerar den en lista med alla 4 nummer användaren gissade om den är av typen gissning. Om det är av typen svårighetsgrad så 
    returnerar den bara användarens input som en sträng.'''
    while True:
        user_input = input(line).strip().lower()
        user_input = user_input.replace(" ", "")
        if validate_input(user_input, input_type):
            if input_type == InputType.GUESS:
                return [int(number) for number in user_input]
            return user_input

def write_output(guesses: list[list[int]], feedback: list[str]) -> None:
    '''
    Skriver ut tabellen vid varje gissning. Den tar in listan med alla gissningar och listan med all feedback. Den kollar sedan så att
    guesses och feedback finns, om man vill skriva en tom tabell går det pga detta, och kollar så att den indexet i for loopen är mindre
    eller lika med antalet gissningar. Detta gör så att gissningarna skrivs ut på rätt rad, från den senaste först till den första gissningen
    sist eftersom den skriver allt uppifrån. I for loopen gör den även om den nuvarande gissningen till en sträng från en lista med integers.
    För att kunna skriva ut den korrekt.'''
    print(f"{"Försök":<20}{"Gissning":<20}{"Feedback"}\n{"-"*50}")
    for i in range(12, 0, -1):
        if guesses and feedback and i <= len(guesses):
            guess = "".join(map(str, guesses[i-1]))
            print(f"{i:>2}{'.':<20}{guess:<20}{" ".join(feedback[i-1])}\n")
        else:
            print(f"{i:>2}{".":<20}{"":<20}{""}\n")

def write_welcome() -> None:
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

def write_win_message() -> None:
    print("Grattis du gissade rätt!")

def write_loss_message() -> None:
    print("Du förlorade, bättre lycka nästa gång!")

def create_number(difficulty: str) -> list[int]:
    '''
    Tar in difficulty, lätt eller svår, och skapar numret med antingen inga upprepningar för lätt svårighetsgrad
    eller eventuellt med upprepningar för svår svårighetsgrad. Den returernar sedan en lista med 4 integers i.
    '''
    number = []
    if difficulty == "svår":
        for i in range(4):
            number.append(random.randint(1,6))
    elif difficulty == "lätt":
        number = random.sample(range(1,7), 4)
    return number

def compare_numbers(correct_number: list[int], user_guess: list[int]) -> list[str]:
    '''
    Jämför det korrekta numret med användarens gissning och returnerar en list med feedbacken som syns i spelet i form av ✔ för
    varje rätt siffra på rätt plats och ☐ för varje rätt siffra på fel plats i ingen speciell ordning.'''
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

def check_win(correct_number: list[int], user_guess: list[int]) -> bool:
    '''
    Kollar om användaren vunnit. Den tar in det korrekta numret och användarens gissning och jämför den. Den returnerar sedan True vid
     vinst och False annars. '''
    return correct_number == user_guess

def game_sequence(correct_number: list[int]) -> bool:
    '''
    Det här är spel loopen, den som körs under spelets gång för alla tolv gissningar. 
    Den frågar först efter användarens gissning med get_input funktionen och lägger sedan till gissningen till 
    listan med alla gissningar. Den skapar sedan feedbacken och lägger till den till listan med all feedback. Sedan skriver den ut
    tabellen och kollar om användaren vann och returnerar då True annars fortsätter den och om alla gissningar tar slut returnerar den
    False.'''
    amount_guesses = 0
    guesses = []
    all_feedback = []

    while amount_guesses < 12:
        user_guess = get_input("Skriv in din gissning\n> ", InputType.GUESS)
        guesses.append(user_guess)
        amount_guesses += 1

        feedback = compare_numbers(correct_number, user_guess)
        all_feedback.append(feedback)
        write_output(guesses, all_feedback)

        if check_win(correct_number, user_guess):
            return True

    return False

def main() -> None:
    '''
    Den här körs i början av spelet och styr hela spelgången. Den börjar med att skriva ut välkomstmeddelandet och fråga efter svårighetsgraden med get_input och typen difficulty.
    Den skapar sedan ett nummer med create_number och skickar in svårighetsgraden som ett argument.
    Sedan kör den game_sequence som returnerar True om användaren vinner och annars False därför sätter den won = game_sequence. Sedan kollar om användaren
    vann eller inte genom att kolla om won == True eller inte och skriver ut rätt meddelandet för antingen vinst eller förlust.'''
    write_welcome()
    difficulty = get_input("Välj svårighetsgrad (lätt, svår)\n> ", InputType.DIFFICULTY)
    correct_number = create_number(difficulty)

    won = game_sequence(correct_number)

    if won:
        write_win_message()
    else:
        write_loss_message()
    

if __name__ == "__main__": #Den gör så att main funktionen körs om programmet startas från denna fil, eftersom hela programmet bara är en fil startas main alltid vid start av programmet.
    main()                 #När en fil körs i python får variabeln __name__ ett värde, och om programet startades från den filen blir värdet __main__, jag utnyttjar detta för att automatiskt köra main funktionen vid start av programmet.

