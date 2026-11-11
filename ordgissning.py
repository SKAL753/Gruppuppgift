words={
    "1": "Ö",
    "2": "RÅ",
    "3": "TUR",
    "4": "BARA",
    "5": "BANAN",
    "6": "SPELAR",
    "7": "MASTERS",
    "8": "ROLIGARE",
    "9": "ROLIGARES",
    "10": "ROLIGARESI"
}
vilket_ord=input("Vilket ord vill du gissa? (1-10): ")
if vilket_ord in words:
    print(f"Du valde ord {vilket_ord}: {words[vilket_ord]}")
    guess = input("Gissa ordet: ").upper()
    if guess == words[vilket_ord]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words[vilket_ord])
else:
    print("Ogiltigt ord. Välj ett ord mellan 1 och 10.")                                        
    print("Du valde ord 4: BARA")
    guess = input("Gissa ordet: ").upper()
    if guess == words["4"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["4"])
elif vilket_ord == "5":
    print("Du valde ord 5: BANAN")
    guess = input("Gissa ordet: ").upper()
    if guess == words["5"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["5"])
elif vilket_ord == "6":
    print("Du valde ord 6: SPELAR")
    guess = input("Gissa ordet: ").upper()
    if guess == words["6"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["6"])
elif vilket_ord == "7":
    print("Du valde ord 7: MASTERS")
    guess = input("Gissa ordet: ").upper()
    if guess == words["7"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["7"])
elif vilket_ord == "8":
    print("Du valde ord 8: ROLIGARE")
    guess = input("Gissa ordet: ").upper()
    if guess == words["8"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["8"])
elif vilket_ord == "9":
    print("Du valde ord 9: ROLIGARES")
    guess = input("Gissa ordet: ").upper()
    if guess == words["9"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["9"])
elif vilket_ord == "10":
    print("Du valde ord 10: ROLIGARESI")
    guess = input("Gissa ordet: ").upper()
    if guess == words["10"]:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", words["10"])