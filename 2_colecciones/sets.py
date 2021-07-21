#Los sets almacenan multiples items en una variable. Están desordenados, items no cambiables y no admite duplicados

miSet = {"manzana", "cereza", "frambuesa"}

print(miSet)

print(len(miSet))

set1 = {1, 2, 3, 4, 5}
set2 = {True, False, False}

set1 = {"abc", 31, True, 40, "cosa"}

print(type(set1))

#Set constructor
esteSet =  set(("hola", "mundo", "cruel"))
print(esteSet)

#Bucle
for x in esteSet:
    print(x)

#Comprobar si existe en el set:
print("hola" in esteSet)

esteSet.add("añadir")
print(esteSet)

#Añadir elementos de un set a otro
set1.update(esteSet)
print(set1)

#Añadir elementos de una lñista a un set
lista = ["lista", "añadir de una lista"]
esteSet.update(lista)
print(esteSet)

#Borrar elemento
esteSet.remove("lista")
print(esteSet)

esteSet.discard("hola")
print(esteSet)

#Borrar el último elemento
otroSet = {"este", "es", "otro", "set"}
print(otroSet)
x = otroSet.pop()
print(x)
print(otroSet)

#Vaciar un set
otroSet.clear()
print(otroSet)

#Para borrar un set:
"""
del otroSet
print(otroSet)
"""

for x in set1:
    print(x)

#update
set3 = {"a", "b" , "c"}
set4 = {1, 2, 3}
set3.update(set4)
print(set3)

#Union
set5 = {"a", "b" , "c"}
set6 = {1, 2, 3}
set7 = set5.union(set6)
print(set7)

#Tanto union como update excluyen los duplicados, para no hacerlo:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)

#Sumetric difference update devuelve los valores que no se repiten:
x.symmetric_difference_update(y)
print(x)

#https://www.w3schools.com/python/python_sets_methods.asp