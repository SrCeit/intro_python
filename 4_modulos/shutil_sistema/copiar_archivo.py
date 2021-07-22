import shutil, os

ruta = os.getcwd() + os.sep #os.sep devuelvo el separador entre direcotios d ela ruta
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'

try:
    shutil.copyfile(origen,destino)
    print("Archivo copiado")
except Exception as e:
    print("Error", e.args)