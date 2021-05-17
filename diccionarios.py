#Almacen datos con key:
esteDiccionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1990
}

print(esteDiccionario)
print(esteDiccionario["marca"])

#Los valores duplicados, sobreescriben al anterior
esteDiccionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1990,
    "año": 2000
}
print(esteDiccionario)
print(len(esteDiccionario))

miDiccionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "electrico": False,
    "año": 1990,
    "colores": ["rojo", "azul", "negro"]
}
print(miDiccionario)
print(type(miDiccionario))

#Sacar un valor:
x = miDiccionario.get("modelo")
print(x)

#Sacar todas las keys
x = miDiccionario.keys()
print(x)

miDiccionario["caballos"] = 320
print(x)

#Obtener valores:
x = miDiccionario.values()
print(x)

x = miDiccionario.items()
miDiccionario["combustible"] = "gasolina"
print(x)

if "combustible" in  miDiccionario:
    print("Si, \'combustible\' está")
else:
    print("No está")

#Cambiar un valor
miDiccionario.update({"año": 2020})
print(miDiccionario)

#Borrar un item especificada
miDiccionario.pop("combustible")
print(miDiccionario)

#Borra el último item insertado
x = miDiccionario.items()
miDiccionario["combustible"] = "gasolina"
print(x)

miDiccionario.popitem()
print(miDiccionario)

#Borrar key con valor
del miDiccionario["modelo"]
print(miDiccionario)

"""
También se puede usar del para borrar el diccionario
del miDiccionario
"""

#Vaciar el diccionario
miDiccionario.clear()
print(miDiccionario)

#Loops
for x in esteDiccionario:
    print(x)

for x in esteDiccionario:
    print(esteDiccionario[x])

for x in esteDiccionario.values():
    print(x)

for x in esteDiccionario.keys():
    print(x)

#Imprimir keys y valores:
for x, y in esteDiccionario.items():
    print(x, y)


#Copiar diccionario
copiarDiccionario = esteDiccionario.copy()
print(copiarDiccionario)

otraCopiaDicc = dict(esteDiccionario)
print(otraCopiaDicc)

#Diccionario que contiene más diccionarios
grupoDiccionario = {
    "casa1": {
        "calle": "La Calle Falsa",
        "precio": 100000
    },
    "casa2": {
        "calle": "La Calle nº 2",
        "precio": 200000
    },
    "casa3": {
        "calle": "La Calle nº 3",
        "precio": 750000
    }
}
print(grupoDiccionario)


#Incluir 3 diccionarios en uno:
casa1 = {
        "calle": "La Calle Falsa",
        "precio": 100000
}
casa2 = {
        "calle": "La Calle nº 2",
        "precio": 200000
}
casa3 = {
        "calle": "La Calle nº 3",
        "precio": 750000
}

grupo2 = {
    "casa1": casa1,
    "casa2": casa2,
    "casa3": casa3
}
print(grupo2)
