import random

passlen = int(input("Introduce la longitud de la contraseña: "))

s = "abcdefghijklmnñopqrstuvwxyz0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@#~^&*()?"
p = "".join(random.sample(s, passlen))

print(p)