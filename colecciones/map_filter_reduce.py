from functools import reduce

#La funcion map(funcion, secuencia) nos permite ejecutar una función a cada uno de los elementos de una secuencia
items = [1, 2, 3, 4, 5]

def sqr(x): 
    return x ** 2

cuadrado = map(sqr, items)

print(list(cuadrado))

#La funcion filter(funcion, secuencia)) devuelve una secuencia filtrando los elementos de otra secuencia dada
lista = [1,2 ,3,4,5,6]

def par(x):
    return x % 2 == 0

pares = list(filter(par, lista))

print(pares)

#La función reduce(funcion, secuencia) devuelve un único valor, resultado de aplicar una función dada a los elementos de una lista (from functools import reduce)
lista = [2, 3, 4]

def potencia(x,y):
    return x**y

resultado = reduce(potencia, lista)

print(resultado)

#List comprehension es parecido a map, pero en vez de ejecutar una función, se aplica una expresión
resultado = [x ** 3 for x in lista]
print(resultado)

resultado = [x for x in range(10) if x % 2 == 0]
print(resultado)

resultado = [x ** y for x in [1,2,3] for y in [4,5,6]]
print(resultado)