#Una variable global es una variable declarada fuera de la funcion y pueden ser usados tanto por las funciones como fuera de ellas

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#Varaible dentro de una funcion con nombre igual que la función global, solo se sobreescribe dentro de la función.
x = "no cambia"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("La variable " + x) 

#Global keyword declarada desde una funcion
def myfunc():
    global x
    x = "dentro de funcion"

myfunc()

print("La global declarada desde " + x) 

#Otro ejemplo de global keyword
x = "no cambia"

def myfunc():
    global x
    x = "ha cambiado"

myfunc()

print("La variable " + x)