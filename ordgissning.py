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
vilket_ord = input("Vilket ord vill du gissa? (1-10): ")

if vilket_ord in words:
    word = words[vilket_ord]
    guessed = []
    wrong = []
    attempts = 9

    print("\nGissa bokstäverna i ordet!")


    while attempts > 0:
        hidden_word=""

        for letter in word:
            if letter in guessed:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "

        print("\nOrdet: ", hidden_word)
        print("försök kvar: ", attempts)
        print("fel gissade bokstäver: ", (wrong))