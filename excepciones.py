while True:
    try:
        x = int(input("Introduce un número:"))
        div = 10/x

        break
    except ValueError as ve:
        print ("Debes introducir un número")
        print(ve)
        print(ve.args)
    except ZeroDivisionError as zero:
        print("No se puede dividir por cero")
        print(zero)
        print(zero.args)
    else:
        print("Otra excepcion")
    finally:
        print("Fin de programa")