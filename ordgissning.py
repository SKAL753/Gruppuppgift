
#Tar ordlista från annan fil, annars blir det galet med bloat.
from ordlista import ordlista
import random
#Svårighetsgrad är proportionell med längden av orden som ska gissas
vilken_svårighetsgrad = input("Vilken svårighetsgrad vill du spela på? (1-10): ").strip()

if vilken_svårighetsgrad.isdigit() and 1 <= int(vilken_svårighetsgrad) <= 10:
    word = random.choice(ordlista[int(vilken_svårighetsgrad)]).upper()

    guessed = []
    wrong = []
    attempts = 9

    print("\nGissa bokstäverna i ordet!")
#Gör så att tomrum byts ut mot bokstäver, den bygger upp en sträng av underscoress en visar de beroende på om de är gissade eller inte. Funegrar också ifall mellanslag skulle läggas till i framtiden.
    while attempts > 0:
        hidden_word = ""
        for letter in word:
            if letter == " ":
                hidden_word += "  "
            elif letter in guessed:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "
#Visar generell info om spelet under dess gång, förklarliga titlar.
        print("\nOrdet:", hidden_word)
        print("Försök kvar:", attempts)
        print("Fel gissade bokstäver:", wrong)
#Kollar om alla ord som är gissade är i ordet, isånafall så säger den grattis.
        if all(letter == " " or letter in guessed for letter in word):
            print("\nGrattis! Du gissade rätt!")
            print("Ordet var:", word)
            break

        gissning = input("Gissa en bokstav: ").strip().upper()
#Inmatningssäkerhet
        if len(gissning) != 1 or not gissning.isalpha():
            print("Vänligen gissa en enda bokstav.")
            continue
        elif gissning in guessed or gissning in wrong:
            print("Du har redan gissat den bokstaven.")
            continue
        elif gissning in word:
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