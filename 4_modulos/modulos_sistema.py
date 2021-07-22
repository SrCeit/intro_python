import os, subprocess, sys

print("Módulo os:")
print("\tSaber si se puede acceder a un archivo o directorio necesitamos path y modo de acceso (os.F_OK, os.R_OK, os.W_OK, os.X_OK)\t:  "
    , os.access(".\\3_ficheros\\ficheros\\escritura.txt", os.F_OK))
print()
print("Obtener el directorio actual ", os.getcwd())
print(dir(os))
print()
print("Directorios ", os.listdir())
print("Con os.system('comando') podemos usar comando del la terminal: ", os.system("ipconfig"))
print("\n")

print("Modulo sys:")
print(sys.version)
print(sys.platform)
print()

print("Modulo subprocess:")
print(subprocess.call("systeminfo"))
salida = subprocess.check_output("dir",shell=True)
print(salida)
