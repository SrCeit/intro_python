import json, xml.etree.cElementTree as e


data_json = '{"nombre":"Pepe", "edad":23 }'
datos = json.loads(data_json)
print(datos)

print("Datos de : https://analisis.datosabiertos.jcyl.es/explore/dataset/vacunas-recibidas-covid/export/?disjunctive.provincia&refine.provincia=Burgos")
with open(".\\3_ficheros\\ficheros\\ficheroJSON.json") as fichero:
    datos=json.load(fichero)
print(datos)

with open(".\\3_ficheros\\ficheros\\json_to_file.txt", "w") as json_file:
    json.dump(datos, json_file, indent =4, sort_keys=True) #Indent es el espacio entre el principio de linea y el siguiente corchete, tanto indent como sort_keys son opcionales

print(json.dumps(datos, indent =4, sort_keys=True)) #Indent es el espacio entre el principio de linea y el siguiente corchete

with open(".\\3_ficheros\\ficheros\\escribir_json.json", "w") as escribir:
    json.dump(datos, escribir)

print()
