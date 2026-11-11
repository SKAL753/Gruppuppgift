word_1="Ö"
word_2="RÅ"
word_3="TUR"
word_4="BARA"
word_5="BANAN"
word_6="SPELAR"
word_7="MASTERS"
word_8="ROLIGARE"
word_9="ROLIGARES"
word_10="ROLIGARESI"
vilket_ord=input("Vilket ord vill du gissa? (1-10): ")
if vilket_ord == "1":
    print("Du valde ord 1: Ö")
    guess = input("Gissa ordet: ").upper()
    if guess == word_1:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", word_1)
elif vilket_ord == "2":
    print("Du valde ord 2: RÅ")
    guess = input("Gissa ordet: ").upper()
    if guess == word_2:
        print("Grattis! Du gissade rätt!")
    else:
        print("Tyvärr, det var fel. Rätt ord var:", word_2)
    