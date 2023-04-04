with open('traza.txt', 'r') as archivo_entrada:
    lineas_entrada = archivo_entrada.readlines()

lineas_salida = []
for i, linea in enumerate(lineas_entrada):
    if "CREATE LASTCHILD OF refError NAMESPACE '' NAME 'Code' VALUE 'GSS-415" in linea:
        for j in range(max(0, i - 25), i):
            if "SET Error = Not" in lineas_entrada[j]:
                error_linea = "415"
                error_index = lineas_entrada[j].find("SET Error = Not")
                linea_salida = error_linea + "-> " + lineas_entrada[j][error_index:]
                lineas_salida.append(linea_salida)
                break
    elif "CREATE LASTCHILD OF refError NAMESPACE '' NAME 'Code' VALUE 'GSS-422" in linea:
        for j in range(max(0, i - 25), i):
            if "SET Error = Not" in lineas_entrada[j]:
                error_linea = "422"
                error_index = lineas_entrada[j].find("SET Error = Not")
                linea_salida = error_linea + "-> " + lineas_entrada[j][error_index:]
                lineas_salida.append(linea_salida)
                break

for i, linea in enumerate(lineas_salida):
    executing_index = linea.rfind("Executing statement")
    if executing_index != -1:
        lineas_salida[i] = linea[0:3] + linea[executing_index:]

with open('archivo_salida.txt', 'w') as archivo_salida:
    archivo_salida.write('-------------------------422 o 415---------------------------\n')
    archivo_salida.write(''.join(lineas_salida))
    archivo_salida.write('-------------------------422 o 415---------------------------')