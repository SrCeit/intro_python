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


'''
Métodos de los strings:

cadena.capitalize    cadena.isalnum       cadena.join          cadena.rsplit
cadena.casefold      cadena.isalpha       cadena.ljust         cadena.rstrip
cadena.center        cadena.isdecimal     cadena.lower         cadena.split
cadena.count         cadena.isdigit       cadena.lstrip        cadena.splitlines
cadena.encode        cadena.isidentifier  cadena.maketrans     cadena.startswith
cadena.endswith      cadena.islower       cadena.partition     cadena.strip
cadena.expandtabs    cadena.isnumeric     cadena.replace       cadena.swapcase
cadena.find          cadena.isprintable   cadena.rfind         cadena.title
cadena.format        cadena.isspace       cadena.rindex        cadena.translate
cadena.format_map    cadena.istitle       cadena.rjust         cadena.upper
cadena.index         cadena.isupper       cadena.rpartition    cadena.zfill

Métodos de formato

cad = "hola, como estás?"
print(cad.capitalize())
Hola, como estás?

cad = "Hola Mundo" 
print(cad.lower())
hola mundo

cad = "hola mundo"
print(cad.upper())
HOLA MUNDO

cad = "Hola Mundo"
print(cad.swapcase())
hOLA mUNDO

cad = "hola mundo"
print(cad.title())
Hola Mundo

print(cad.center(50))
                    hola mundo                    
print(cad.center(50,"="))
====================hola mundo====================

print(cad.ljust(50,"="))
hola mundo========================================
print(cad.rjust(50,"="))
========================================hola mundo

num = 123
print(str(num).zfill(12))
000000000123

Métodos de búsqueda

cad = "bienvenido a mi aplicación"
cad.count("a")

cad.count("a",16)

cad.count("a",10,16)


cad.find("mi")

cad.find("hola")


cad.rfind("a")


El método index() y rindex() son similares a los anteriores pero provocan una excepción ValueError cuando no encuentra la subcadena.
Métodos de validación

cad.startswith("b")

cad.startswith("m")

cad.startswith("m",13)


cad.endswith("ción")

cad.endswith("ción",0,10)

cad.endswith("nido",0,10)


Otras funciones de validación: isalnum(), isalpha(), isdigit(), islower(), isupper(), isspace(), istitle(),…
Métodos de sustitución
format

En la unidad “Entrada y salida estándar” ya estuvimos introduciendo el concepto de formateo de la cadenas. Estuvimos viendo que hay dos métodos y vimos algunos ejemplos del nuevo estilo con la función predefinida format().

El uso del estilo nuevo es actualmente el recomendado (puedes obtener más información y ejemplos en algunos de estos enlaces: enlace1 y enlace2) y obtiene toda su potencialidad usando el método format() de las cadenas. Veamos algunos ejemplos:

'{} {}'.format("a", "b")
'a b'
'{1} {0}'.format("a", "b")
'b a'
'Coordenadas: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordenadas: 37.24N, -115.81W'
'{0:b} {1:x} {2:.2f}'.format(123, 223,12.2345)
'1111011 df 12.23'
'{:^10}'.format('test')
'   test   '

Otros métodos de sustitución

buscar = "nombre apellido"
reemplazar_por = "Juan Pérez" 
print ("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)) 
Estimado Sr. Juan Pérez:

cadena = "   www.eugeniabahit.com   " 
print(cadena.strip())
www.eugeniabahit.com
cadena="00000000123000000000"
print(cadena.strip("0"))
123

De forma similar lstrip(["caracter"]) y rstrip(["caracter"]).
Métodos de unión y división

formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")"
print("275".join(formato_numero_factura))
Nº 0000-0275-0000 (ID: 275)

hora = "12:23"
print(hora.rpartition(":"))

print(hora.partition(":"))

hora = "12:23:12"
print(hora.partition(":"))

print(hora.split(":"))

print(hora.rpartition(":"))

print(hora.rsplit(":",1))


texto = "Linea 1\nLinea 2\nLinea 3" 
print(texto.splitlines())
#['Linea 1', 'Linea 2', 'Linea 3']


'''