
# Tar ordlista från annan fil, annars blir det galet med bloat.
from ordlista import ordlista
import random


# Inmatningssäkerhet
def kontrollera_gissning(rätt_gissade_bokstäver, fel_gissade_bokstäver):
    gissad_bokstav = input("Gissa en bokstav: ").strip().upper()

    if len(gissad_bokstav) != 1 or not gissad_bokstav.isalpha():
        print("Vänligen gissa en enda bokstav.")
        return None

    elif gissad_bokstav in rätt_gissade_bokstäver or gissad_bokstav in fel_gissade_bokstäver:
        print("Du har redan gissat den bokstaven.")
        return None

    return gissad_bokstav


# Bygger upp och visar ordet med dolda och gissade bokstäver
def visa_ord(hemligt_ord, rätt_gissade_bokstäver):
    dolt_ord = ""

    for bokstav in hemligt_ord:
        if bokstav == " ":
            dolt_ord += "  "
        elif bokstav in ratt_gissade_bokstaver:
            dolt_ord += bokstav + " "
        else:
            dolt_ord += "_ "

    print("\nOrdet:", dolt_ord)


# Visar generell information om spelet
def visa_spelstatus(antal_forsök_kvar, fel_gissade_bokstäver):
    print("Försök kvar:", antal_försök_kvar)
    print("Fel gissade bokstäver:", fel_gissade_bokstäver)


# Kontrollerar om hela ordet är gissat
def ar_ordet_gissat(hemligt_ord, rätt_gissade_bokstäver):
    return all(
        bokstav == " " or bokstav in rätt_gissade_bokstäer
        for bokstav in hemligt_ord
    )


# Svårighetsgrad är proportionell med längden av orden som ska gissas
vald_svårighetsgrad = input(
    "Vilken svårighetsgrad vill du spela på? (1-10): "
).strip()

if vald_svårighetsgrad.isdigit() and 1 <= int(vald_svårighetsgrad) <= 10:

    hemligt_ord = random.choice(ordlista[int(vald_svårighetsgrad)]).upper()

    rätt_gissade_bokstäver = []
    fel_gissade_bokstäver = []
    antal_försök_kvar = 9

    print("\nGissa bokstäverna i ordet!")

    while antal_forsok_kvar > 0:

        # Visar ordet och spelinformation
        visa_ord(hemligt_ord, rätt_gissade_bokstäver)
        visa_spelstatus(antal_försök_kvar, fel_gissade_bokstäver)

        # Kollar om alla bokstäver är gissade
        if ar_ordet_gissat(hemligt_ord, rätt_gissade_bokstäver):
            print("\nGrattis! Du gissade rätt!")
            print("Ordet var:", hemligt_ord)
            break

        # Hämtar och kontrollerar användarens gissning
        gissad_bokstav = kontrollera_gissning(
            rätt_gissade_bokstäver,
            fel_gissade_bokstaver
        )

        if gissad_bokstav is None:
            continue

        if gissad_bokstav in hemligt_ord:
            rätt_gissade_bokstäver.append(gissad_bokstav)
            print("Rätt gissat!")

        else:
            fel_gissade_bokstaver.append(gissad_bokstav)
            antal_försök_kvar -= 1
            print("Fel gissat!")

    else:
        print("\nDu har slut på försök!")
        print("Rätt ord var:", hemligt_ord)

else:
    print("Ogiltig svårighetsgrad. Välj ett tal mellan 1 och 10.")
