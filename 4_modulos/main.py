import operaciones as opr #Importamos el módulo que hemos creado operaciones.py para poder usar su contenido

print(opr.cuadrado(2))
continuar = True

while continuar:
    try:

        base = int(input("Escribe la base: "))
        exponente = int(input("Escribe el exponente: "))
        print(opr.enesima(base, exponente))

        opcion = input("¿Salir? (Y/N): ")
        
        if opcion.lower() == "y":
            print("Ejecución finalizada")
            break
        else:
            continue
        

    except ValueError as ve:
        print ("Debes introducir un número")
        print(ve)
        
    except Exception as e:
        print(type(e))
        print(e)
        print(e.args)     
    