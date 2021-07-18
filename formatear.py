#Modificar la salida de los datos:
print("El resultado: %d %f %s" %  (2.5,2.345,2.5))

print("El resultado con dos decimales en el float: %d %.2f %s" %  (2.5,2.345,2.5))

print("String, octal y binario: %s %o %x" % (bin(31), 31, 31))

print("El producto %s cantidad = %d precio = %.2f" % ("cesta",23, 13.323))

#Función format():
print("Ahora usamos la función format con 31 en binatrio, octal y hexadecimal: ", format(31,"b"), format(31, "o"), format(31, "x"))

print("Float con dos decimales: ", format(2.4384, "0.2f"))