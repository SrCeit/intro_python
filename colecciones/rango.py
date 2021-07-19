#Los rangos son una secuencia de numeros que se suelen utilizar en los bucles
rango = range(0,13, 2) #Comienza desde el 0 y va hasta el 12 de 2 en 2
type(rango)
print(rango.start)
print(rango.stop)
print(rango.step)
print("longitud del rango", len(rango))
print("longitud del rango", max(rango))
print("longitud del rango", min(rango))
print("longitud del rango", sum(rango))
print("longitud del rango", sorted(rango))



#Se pueden comvertir en lista
lista = list(rango)
print(lista)

print(list(range(10)))

print(list(range(1,11)))

print(list(range(-10, 0, 1)))

print(list(range(0, -10, -1)))

#Recorrido
for i in range(-20, 0, 1):
    print(i, end= "")
