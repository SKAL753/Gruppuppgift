# Tar ordlista från annan fil, annars blir det galet med bloat.
from ordlista import ordlista
import random


# Inmatningssäkerhet
def kontrollera_gissning(guessed, wrong):
    gissning = input("Gissa en bokstav: ").strip().upper()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Vänligen gissa en enda bokstav.")
        return None

    elif gissning in guessed or gissning in wrong:
        print("Du har redan gissat den bokstaven.")
        return None

    return gissning


# Bygger upp och visar ordet med dolda och gissade bokstäver
def visa_ord(word, guessed):
    hidden_word = ""

    for letter in word:
        if letter == " ":
            hidden_word += "  "
        elif letter in guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "

    print("\nOrdet:", hidden_word)


# Visar generell information om spelet
def visa_status(attempts, wrong):
    print("Försök kvar:", attempts)
    print("Fel gissade bokstäver:", wrong)


# Kontrollerar om hela ordet är gissat
def ar_ordet_gissat(word, guessed):
    return all(letter == " " or letter in guessed for letter in word)


# Svårighetsgrad är proportionell med längden av orden som ska gissas
vilken_svårighetsgrad = input("Vilken svårighetsgrad vill du spela på? (1-10): ").strip()

if vilken_svårighetsgrad.isdigit() and 1 <= int(vilken_svårighetsgrad) <= 10:

    word = random.choice(ordlista[int(vilken_svårighetsgrad)]).upper()

    guessed = []
    wrong = []
    attempts = 9

    print("\nGissa bokstäverna i ordet!")

    while attempts > 0:

        # Visar ordet och spelinformation
        visa_ord(word, guessed)
        visa_status(attempts, wrong)

        # Kollar om alla bokstäver är gissade
        if ar_ordet_gissat(word, guessed):
            print("\nGrattis! Du gissade rätt!")
            print("Ordet var:", word)
            break

        # Hämtar och kontrollerar användarens gissning
        gissning = kontrollera_gissning(guessed, wrong)

        if gissning is None:
            continue

        if gissning in word:
            guessed.append(gissning)
            print("Rätt gissat!")

        else:
            wrong.append(gissning)
            attempts -= 1
            print("Fel gissat!")

    else:
        print("\nDu har slut på försök!")
        print("Rätt ord var:", word)

else:
    print("Ogiltig svårighetsgrad. Välj ett tal mellan 1 och 10.")
