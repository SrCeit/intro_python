#String multilinea con comilla doble o simple
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

#Imprimir una parte de un string:
b = "Hello, World!"
print(b[2:5])

#Los primeros x digitos:
b = "Hello, World!"
print(b[:5])

#Imprimir desde los primeros x digitos:
b = "Hello, World!"
print(b[5:])

#Desde la posición -5 (contar desde el final hacia principio) hasta la -2
b = "Hello, World!"
print(b[-5:-2])

#https://www.w3schools.com/python/python_ref_string.asp

#Concatenar
a = "Hola"
b = "Mundo"
c = a + ", " + b
print(c)

#Longitud
print(len(c))

#Imprimir una posición, la posicion 0 corresponde a la primera letra
print(c[0])

#Linea a linea
for z in c:
    print(z)

#Comprobar si un string contiene a otro, devuelve True o False
txt = "The best things in life are free!"
print("free" in txt)
print("free" not in txt)

#In y not in dentro de un if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

#Caracteres prohibidos
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt2 = "Otros tipos de caracteres prohibidos: comilla simple: \' barra invertida \\ ey, un salto de linea\nuna tabulación\t coche. Aqui \bno \bhay \bespacio"
print(txt2)

#Otros: \r \f (formulario), \ooo (octal), \xhh

#CONCATENAR
"""
Esto alnza un ERROR
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

age = 36

txt = "My name is John, and I am {}"
print(txt.format(age))

cantidad = 3
id_item = 567
precio = 49.95

myorder = "Quiero {} piezas del item {} por {} euros."
print(myorder.format(cantidad, id_item, precio))

#También podemos cambiar el orden de aparicion de los parametros en el string

myorder = "Voy a pagar {2} euros por {0} piezas del item {1}."
print(myorder.format(cantidad, id_item, precio))

#Metodos de strings

#La primera en mayuscula con capitalize
txt = "no se me ocurre nada que poner"
x = txt.capitalize()
print(x)

#La primera en minuscula con casefold
txt = "No se me ocurre nada que poner"
x = txt.casefold()
print(x)

#Centrar
txt = "Simba"
x = txt.center(20)
print(x) 

#La primera letra de cada palabra en mayúscula
txt = "Welcome to my world"
x = txt.title()
print(x)

#Contar palabras
txt = "Esto sirve para contar las veces que aparece la palabra \"que\""
x = txt.count("que")
print(x)

#Codificar, si no se especifica se utiliza UTF-8
txt = "Me llamo Rubén"
x = txt.encode()
print(x)

#Mayusculas y minusculas0
a = "mayusculas!"
print(a.upper())

a = "MINUSCULAS!"
print(a.lower())

#Borrar los espacios en blanco iniciales y finales  con split()
a = " Sin espacios al pricipio y final "
print(a.strip())  

#Separa los strings en substrings cuando hay una coma
a = "Hello, World, en, Python!"
print(a.split(","))

a = "\u0033" #con unicode, unicode para 3
print(a.isdecimal())

a = "23" #Numeros como -1 y 1.5 no son considerados numericos ya que tienen caracteres no numéricos
print(a.isnumeric())

#https://www.w3schools.com/python/python_ref_string.asp




