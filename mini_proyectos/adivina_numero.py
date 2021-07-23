import random

num = random.randint(1,10)
for i in range(0, 3):
    a = int(input("Adivina el número: "))
    if a == num:
        print("Has ganado!")
        print(f"El numero era: ")
        break
    elif a < num:
        print("El número es mayor")
    else:
        print("El número es menor")

if a != num:
    print("Has perdido, el número era: ", num)
