#Tipos de datos en python

#String
x = "Hello World" #O en su defecto, x = str("Hello World")
print(x)
print(type(x))

x = str(3)
print(x)
print(type(x))

#Integer
x = 20 #O en su defecto, x = int(20)
print(x)
print(type(x))

x = int(2.8) #Estos sera x = 2 a la hora de imprimir
print(x)

#float
x = 20.5 
print(x)
print(type(x))

y = float(20)
print(y)
print(type(y))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Números complejos
x = 2 + 1j
print(x)
print(type(x))

y = 2 - 1j
result = x * y
print(result)

#Lista 
x = ["manzana", "banana", "cereza"]
#O es su defecto x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

#Tupla
x = ("manzana", "pera", "frambuesa")
#O en su defcto, x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

#Rango
x = range(9)
print(x)
print(type(x))

#Dictado o dict
x = {"nombre" : "John", "edad" : 36}
#O es su defecto x = dict(nombre="John", edad=36)
print(x)
print(type(x))

#Set
x = {"Apple", "Google", "Microsoft"}
#O es su defecto x = set(("Apple", ""Google", "Microsft"))
print(x)
print(type(x))

#Frozenset
x = frozenset({"Apple", "Google", "Microsoft"})
#O es su defecto x = frozenset(("Apple", ""Google", "Microsft"))
print(x)
print(type(x))

#Booleano
x = True
y = False
print(x,y)
print(type(x))

x = bool(5)
print("Si x es 5 entonces su booleano es:", x)
print("Valor de y no varia:", y)
print(type(x))

#Bytes
x = b"Hola, Mundo"
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

#Bytearray
x = bytearray(5)
print(x)
print(type(x))

#MemoryView
x = memoryview(bytes(5))
print(x)
print(type(x))

#Encode y decode
byte1 = bytes("piña", "latin1")
print(byte1)
print(byte1.decode("utf-8", "ignore"))

byte1 = bytes("piña", "latin1")
print(byte1.decode("utf-8", "replace"))

cad = "piña"
byte1 = cad.encode("utf-8")
print("Utilizando cad.encode('utf-8') ", byte1) #Convertir una cadena unicode a bytes

print("Utilizando cad.decode('utf-8') ", byte1.decode("utf-8")) #De bytes a unicode

#Binario, octal y hexadecimal
print("El binario de 18: ", bin(18))

print("El octal de 18: ", oct(18))

print("El hexadecimal de 18: ", hex(18))
