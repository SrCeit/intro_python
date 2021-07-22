'''
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena.
Por ejemplo, si recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1
'''
dict = {}
frase = input("Frase:")
lista_palabras=frase.split(" ")
for palabra in lista_palabras:
    if palabra in dict:
        dict[palabra]+=1
    else:
        dict[palabra]=1    

for campo,valor in dict.items():
    print (campo,"->",valor)
print()

'''
Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. 
Escribir un programa que lea una palabra y la muestre usando el código morse.
'''
codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}    

palabra = input("Palabra:")
lista_codigos = []
for caracter in palabra:
    if caracter.islower():
        caracter=caracter.upper()
    lista_codigos.append(codigo[caracter])    
print (" ".join(lista_codigos))
print()

'''
Suponga un diccionario que contiene como clave el nombre de una persona y como valor una lista con todas sus “gustos”. 
Desarrolle un programa que agregue “gustos” a la persona:
'''
gustos={}
nombre = input("Nombre:")
while nombre!="*":
    gusto=input("Gusto:")
    lista_gustos=gustos.setdefault(nombre,[gusto]) #setdafault añade una key y un valor al diccionario
    if lista_gustos!=[gusto]:
        gustos[nombre].append(gusto)
    nombre = input("Nombre:")
print(gustos)