#Los decoradores son funciones que reciben como parámeteros otras funciones y devuelve una función.
def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:'%tabla)
        for numero in range(0,11):
            funcion(numero,tabla)
        print('-' * 15)
    return envoltura

@tablas #Esto es un decorador que manda la funcion suma a la función tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas #Esto es un decorador que manda la multiplicar suma a la función tablas
def multiplicar(numero, tabla=1):
    print('%2i x %2i = %3i' %(tabla, numero, tabla*numero))

#Ejemplo:
for x in range(0,11):
    multiplicar(x)
print("Fin!")
