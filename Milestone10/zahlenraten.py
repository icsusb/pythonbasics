# Teilnehmer :  Alex ; Axel ; Dieter ; Melinda ; Ralf ; Steffen


import random
n = random.randint(1, 10)
guess = int(input("Gib eine Zahl von 1 bis 10: "))
while n != "Rate":
    print
    if guess < n:
        print("zu klein")
        guess = int(input("Gib eine Zahl von 1 bis 10: "))
    elif guess > n:
        print("Zahl zu groß")
        guess = int(input("Gib eine Zahl von 1 bis 10: "))
    else:
        print("RICHTIG!!!!")
        break
    print

