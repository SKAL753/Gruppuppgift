import random
#Valsystem och vad som vinner
val=["sten","sax","påse"]
points=0
cpupoints=0
wincondition = {
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"
}
#variablar för vad datorn väljer respektive spelaren
cpuchoice = ""
pchoice = ""
#start på spelet
print("Nu ska vi spela Sten, Sax eller Påse!\n\nJag är python311\n")
user = input("Ange användarnamn ---> ")
#hindrar inmatningsfel
while True:
    try:
        repeat = int(input("\nHur många omgångar vill du köra? ---> "))
        break
    except ValueError:
        continue
#spel loopen
while True:
    for i in range(repeat):
        
        print(f"\nspelomgång {i+1}\n{(11+len(str(i+1)))*"-"}")
        cpuchoice = random.choice(val)
        while True:
           #Kollar spelarens val, och ser till så att svaret är gilltigt
            pchoice = input("Välj 'Sten', 'Sax' eller 'Påse' ---> ").lower()
            if pchoice not in val:
                continue
            else:
                break
       #kollar vem som vunnit
        if pchoice == cpuchoice:
            print(f"\nOavgjort!\n\n{user}: {pchoice}\nPython311:{cpuchoice}")
        elif wincondition[pchoice] == cpuchoice:
            print(f"\nDu vann!\n\n{user}: {pchoice}\nPython311:{cpuchoice}")
            points+=1
        else:
            print(f"\nDu Förlorade!\n\n{user}: {pchoice}\nPython311:{cpuchoice}")
            cpupoints+=1
    #Kollar vem som van hela matchen
    if points > cpupoints:
        print("\nDu vann matchen!\n")
    elif points == cpupoints:
        print("\nDet blev oavgjort!\n")
    else:
        print("\nDu förlorade matchen!\n")
    print(f"Du fick {points} poäng\n Python311 fick {cpupoints} poäng\n")
    play_again = input("Vill du spela igen? J/N ---> ").lower()
    if play_again in ["ja", "j"]:
        repeat = int(input("\nHur många omgångar vill du köra? ---> "))
        continue
    else:
        break
    