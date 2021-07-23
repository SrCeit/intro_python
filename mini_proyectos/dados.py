import random
while True:
    print(''' 1. Tirar el dado   2. Salir    ''')
    a = int(input("Qé opción eliges?\n"))
    if a == 1:
        number = random.randint(1,6)
        print("Ha salido ",number)
    else:
        break