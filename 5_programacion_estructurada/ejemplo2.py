#!/usr/bin/env python
def sumar(n,*args): #Mínimo un argumento y luego guarda el resto como tupla
	resultado=n
	for i in args:
		resultado+=i
	return resultado

def sumar2(*args): #No hay un mínimo, en caso de no pasar argyumento el resultado será cero.
	resultado=0
	for i in args:
		resultado+=i
	return resultado

def saludar(nombre = "Kelsier", **kwargs): #Nombre por defecto y con los dos asteriscos indicamos un numero n de parametros con keywords, definido como un diccionario
	cadena=nombre
	for valor in kwargs.values():
		cadena+=" " +valor
	return "Hola, "+ cadena

print(sumar(1,3,5,66,7,85,5))

print(sumar2(), sumar2(2,4,6,7,8))

datos = {"nombre":"Jose","nombre2":"Maria","nombre3":"Carlos"}
print(datos)

print(saludar(**datos))