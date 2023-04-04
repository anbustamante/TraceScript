with open('traza.txt', 'r') as archivo_entrada:
    lineas_entrada = archivo_entrada.readlines()

lineas_salida = []
for i, linea in enumerate(lineas_entrada):
    if "CREATE LASTCHILD OF refError NAMESPACE '' NAME 'Code' VALUE 'GSS-415" in linea:
        for j in range(max(0, i - 20), i):
            if "SET Error = Not" in lineas_entrada[j]:
                lineas_salida.append("415: " + lineas_entrada[j])
                break
    elif "CREATE LASTCHILD OF refError NAMESPACE '' NAME 'Code' VALUE 'GSS-422" in linea:
        for j in range(max(0, i - 20), i):
            if "SET Error = Not" in lineas_entrada[j]:
                lineas_salida.append("422: " + lineas_entrada[j])
                break

with open('archivo_salida.txt', 'w') as archivo_salida:
    archivo_salida.write('\n'.join(lineas_salida))