import random
val=["sten","sax","påse"]
cpuchoice = ""
pchoice = ""
print("Nu ska vi spela Sten, Sax eller Påse!\nJag är python311\n")
user = input("Ange användarnamn --->")
repeat = int(input("Hur många omgångar vill du köra? --->"))

for i in range(repeat):
    
    print(f"spelomgång {i+1}\n{(11+len(str(i+1)))*"-"}")
    cpuchoice = random.sample(val,k=1)
    while True:
        pchoice = input("Välj 'Sten', 'Sax' eller 'Påse' --->").lower()
        if pchoice not in val:
            continue
        else:
            break