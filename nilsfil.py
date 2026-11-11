
import random

code = random.sample(["1", "2", "3", "4","5","6"], 4)

print("yo dags att spela")
print("gissa koden med 4 siffror 1, 2, 3, 4")

for i in range(10):
    guess = input("gissa: ").upper()

    if guess == "".join(code):
        print("grattis!")
        break
    else:
        correct = 0
        count=0

        for j in range(4):
            if guess[j] in code:
                count+=1
            if guess[j] == code[j]:
                correct += 1

        print("rätt pos:", correct)
        print("rätt siffra:", count)
else:
    print("du förlorade!")
    print("koden va:", "".join(code))
