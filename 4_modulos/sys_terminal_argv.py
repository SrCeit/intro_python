import sys

print("Entra en la terminal y escribe: py sys_terminal_argv.py num1 num2 num3 ... numN")
print("Has introducido",len(sys.argv),"argumentos")
print(sys.argv)
suma = 0
for i in range(1, len(sys.argv)):
    suma = suma + int (sys.argv[i])
print("La suma es", suma)