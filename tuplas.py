#Ver antes el archivo listas.py
#Las tuple son colecciones de datos ordenadas y no cambiables(no se puueden añadir ni remover elementos).
miTuple = ("Rodolfo", "Katy", "Kike")
print(miTuple)

#Metodo len()
print(len(miTuple))

#Varios tipos de datos en una misma tuple
tuple1 = ("hola", 12, True, "café", 2.85)
print(tuple1)
print(type(tuple1))

#Usar metodo tuple() para crear otra
tuple2 = tuple(("Asi", "creamos", "una", "tuple", "usando", "metodo tuple()"))
print(tuple2)
print("")
#Imprimimos el primer elemento de la tupla
print(tuple1[0])
#Elemento final
print(tuple1[-1])
print("")
#Rango de indices
print(tuple1)
print(tuple1[0:3])
print(tuple1[:2])
print(tuple1[2:])
print(tuple1[-4:-1])
print("")
if "hola" in tuple1:
    print("\'hola\' esta en tuple1")
print("")
#Para mdificar una tuple debemos transofrmarla en una lista
x = ("cafe", "té", "cerveza", "vino")
print(x)
y = list(x)
y[1] = "infusión"
x = tuple(y)

print("Hemos cambiado té por infusión ",x)
print("")
#Para añadir elementos hacemos lo mismo, convertimos la tuple a list
x = ("manzana", "platano", "uva")
print(x)
y = list(x)
y.append("melocotón")
x= tuple(y)
print(x)
print("")
#Borrar elemento
y = list(x)
y.remove("uva")
x = tuple(y)
print(x)
print("")
#Elimina tupla
del x
#Si hacemos print(x) saltara un error ya que ha sido eliminada

#Separar una tupla
frutas = ("Manzana", "Platana", "Cereza")
(verde, amarillo, rojo) = frutas
print(verde)
print(amarillo)
print(rojo)
print("")
#Colocando un asterisco antes del atributo seleccionamos todos los siguientes elements de la tupla
frutas = ("Manzana", "Platana", "Cereza", "Fresa", "Frambuesa")
(verde, amarillo, *rojo) = frutas
print(verde)
print(amarillo)
print(rojo)
print("")
frutas = ("manzana", "mango", "papaya", "piña", "cereza")

(verde, *tropical, rojo) = frutas

print(verde)
print(tropical)
print(rojo)
print("")

#Loops
for x in frutas:
    print(x)

print("")

for i in range(len(frutas)):
    print(frutas[i])
print("\n")

i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

#Union de tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print("")

#Multiplicar tuplas
print("Tupla de frutas original", frutas)
miTupla = frutas * 2
print("Tupla de frutas multiplicada por 2", miTupla)
print("")

#Metodo count() para ver cuantas veces hay un elemento
c = miTupla.count("papaya")
print(c)
print("")

#Método index() devuelve la posicion de un eleento
c = miTupla.index("manzana")
print(c)

