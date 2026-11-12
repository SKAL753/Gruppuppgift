from ordlista import ordlista
import random
vilken_svårighetsgrad = input("Vilken svårighetsgrad vill du spela på? (1-10): ")

if vilken_svårighetsgrad.isdigit() and 1 <= int(vilken_svårighetsgrad) <= 10:
    word = random.choice(ordlista[int(vilken_svårighetsgrad)])
    guessed = []
    wrong = []
    attempts = 9

    print("\nGissa bokstäverna i ordet!")

    while attempts > 0:
        hidden_word = ""

        for letter in word:
            if letter in guessed:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "

        print("\nOrdet:", hidden_word)
        print("Försök kvar:", attempts)
        print("Fel gissade bokstäver:", wrong)

        if all(letter in guessed for letter in word):
            print("\nGrattis! Du gissade rätt!")
            print("Ordet var:", word)
            break

        gissning = input("Gissa en bokstav: ").upper()

        if len(gissning) != 1 or not gissning.isalpha():
            print("Vänligen gissa en enda bokstav.")
            continue
        elif gissning in guessed or gissning in wrong:
            print("Du har redan gissat den bokstaven.")
            continue
        elif gissning in word:
            guessed.append(gissning)
            print("Rätt gissat!")
        elif gissning not in word:
            wrong.append(gissning)
            attempts -= 1
            print("Fel gissat!")
    else:
        print("\nDu har slut på försök!")
        print("Rätt ord var:", word)
else:
    print("Ogiltigt ord. Välj ett ord mellan 1 och 10.")
