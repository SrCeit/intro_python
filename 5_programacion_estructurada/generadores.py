import sys

def par(inicio,fin):
    for i in range(inicio,fin):
        if i % 2 == 0:
            yield i

datos = par(0,17)

for i in datos:
    print(i, end= " ")

while True:
    try:
        print(next(datos), end=" ")
    except StopIteration:
        sys.exit()
