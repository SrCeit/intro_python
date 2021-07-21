f = open(".\\3_ficheros\\ficheros\\lectura.txt")
print(f.read())

print("Ahora leemos una linea completa readline()")
print(f.readline())
f.close()

fichero = open(".\\3_ficheros\\ficheros\\escritura.txt", "w")
fichero.write("Machacamos el contenido del fichero si en la función open escribirmos 'w'\n")
fichero.close()

fichero = open(".\\3_ficheros\\ficheros\\escritura.txt")
print(fichero.read())
fichero.close()

fichero = open(".\\3_ficheros\\ficheros\\escritura.txt", "a")
fichero.write("Para escribir al final de un fichero que ya existe utilizamos 'a'")
fichero.close()
fichero = open(".\\3_ficheros\\ficheros\\escritura.txt")
print(fichero.read())
fichero.close()

if __name__ == "__main__":
   f = open(".\\3_ficheros\\ficheros\\origen.txt")
   g = open(".\\3_ficheros\\ficheros\\destino.txt","w")
   linea = f.readline()
   while linea != "":
      g.write(linea)
      linea = f.readline()
   g.close()
   f.close()

print()

print("Comprobamos si el fichero origen.txt se copio en destino.txt")
g = open(".\\3_ficheros\\ficheros\\destino.txt")
print(g.read())
g.close()
