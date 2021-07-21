import csv

fichero = open(".\\3_ficheros\\ficheros\\fichero.csv")
contenido = csv.reader(fichero)

for row in contenido:
    print("Fila " + str(contenido.line_num) + " " + str(row))
print()  
fichero.close()

fichero = open(".\\3_ficheros\\ficheros\\fichero.csv")
contenido = csv.reader(fichero)

datos = list(contenido)
print(datos, "\n")

print(datos[0][0], "\n")
fichero.close()

with open(".\\3_ficheros\\ficheros\\ficheroCSV.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for fila in csv_reader:
        if line_count == 0:
            print(f'Las columnas: {"    |    " .join(fila)}') 
            line_count += 1
        else:
            
            print(f'\t{fila}')
            print(f'\t{fila[0]} works in the {fila[1]} department, and was born in {fila[2]}.')
            line_count += 1
    print(f'Total: {line_count} lineas')

with open('.\\3_ficheros\\ficheros\\ficheroCSV.txt', mode='r') as csv_file:
    csv_reader2 = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader2:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Fecha"]} , {row["Fruta"]} , {row["Stock"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    print()

    print("Escribir ficheros CSV:")

with open('.\\3_ficheros\\ficheros\\escribirCSV.csv', mode='w') as csv_file:
    csv_file = csv.writer(csv_file, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    csv_file.writerow(['4/5/2015 13:34', 'Apples', '73'])

    
with open('.\\3_ficheros\\ficheros\\escribirCSV.csv', 'a') as fichero:
    contenido = csv.writer(fichero)
    contenido.writerow(['4/5/2015 13:34', 'Apples', '73'])
    contenido.writerows([['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14']])









