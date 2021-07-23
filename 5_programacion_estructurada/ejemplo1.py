#!/usr/bin/env python
def operar(n1,n2,operador='+',respuesta='El resultado es '):
	if operador=="+":
		return respuesta+str(n1+n2)
	elif operador=="-":
		return respuesta+str(n1-n2)
	else:
		return "Error"

def operar2(n1,n2,*,operador='+',respuesta='El resultado es '):
	if operador=="+":
		return respuesta+str(n1+n2)
	elif operador=="-":
		return respuesta+str(n1-n2)
	else:
		return "Error"

def operar3(n1,n2):
	return(n1+n2, n1-n2, n1*n2, n1//n2)

print(operar(6,4,"-"))
print()
print(operar2(6,6,operador="+"))

suma, resta, multiplicacion, division = operar3(6,4) #Es una tupla
print(suma, resta, multiplicacion, division)

