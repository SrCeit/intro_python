import json

data_json = '{"nombre":"Pepe", "edad":23 }'
datos = json.loads(data_json)

with open("\\3_ficheros\\ficheros\\ficheroJSON.json") as fichero:
    datos=json.load(fichero)
print(datos)