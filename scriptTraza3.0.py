import json

with open('traza.txt', 'r') as archivo_entrada:
    lineas_entrada = archivo_entrada.readlines()

lineas_salida = []
lineashttp = []
result = {}
errores = []

                
        
for i, linea in enumerate(lineas_entrada):
    hayError_flag = False
    if "NAME 'Code' VALUE 'GSS-415" in linea:
        for j in range(max(0, i - 20), i):
            if "SET Error = Not" in lineas_entrada[j]:
                error_linea = 415
                trace_line = lineas_entrada[j]
                hayError_flag = True
                #Para añadir al JSON
                error = {
                    "errorCode" : error_linea,
                    "errorLine" : trace_line
                }
                errores.append(error) 
                break
        if not hayError_flag:
            error = {
                "errorCode" : error_linea,
                "errorLine" : "Error especifico"
            }
            errores.append(error) 
        

               
    elif "NAME 'Code' VALUE 'GSS-422" in linea:
        for j in range(max(0, i - 20), i):
            if "SET Error = Not" in lineas_entrada[j]:
                error_linea = 422
                trace_line = lineas_entrada[j]
                hayError_flag = True
               #Para añadir al JSON
                error = {
                    "errorCode" : error_linea,
                    "errorLine" : trace_line
                }
                errores.append(error) 
                break
        if not hayError_flag:
            error = {
                "errorCode" : error_linea,
                "errorLine" : "Error especifico"
            }
            errores.append(error) 
                
        break
    elif "NAME 'Code' VALUE 'GSS-400" in linea:
        for j in range(max(0, i - 20), i):
            if "The result was" in lineas_entrada[j]:
                error_linea = 400
                error_index = lineas_entrada[j].find("Value=NULL")
                linea_salida = error_linea + "\t\t| " + lineas_entrada[j][error_index:]
                result_index2 = linea_salida.find("at (\'")
                linea_salida = linea_salida[:result_index2]
                lineas_salida.append(linea_salida)
                 #Para añadir al JSON
                error = {
                    "errorCode" : error_linea,
                    "errorLine" : lineas_entrada[j]
                }
                errores.append(error)
                break

    elif "This resolved to ''mandatoryCoreId''. The result was" in linea:
        mandatoryCoreId = (lineas_entrada[i]) 
        index = mandatoryCoreId.find("The result was") + len("The result was")
        mandatoryCoreId = mandatoryCoreId[index:]
        index2 = mandatoryCoreId.find("\'\'")
        mandatoryCoreId = mandatoryCoreId[:index2]
    elif "HTTP status code:" in linea:
        httpstatuscode = (lineas_entrada[i]) 
        indexstatuscode = httpstatuscode.find("code: \'\'") + len("code: \'\'")
        httpstatuscode = httpstatuscode[indexstatuscode:-5]

        urlstatuscode = (lineas_entrada[i-1]) 
        indexurl = urlstatuscode.find("URL: \'\'") + len("URL: \'\'")
        urlstatuscode  =  urlstatuscode[indexurl:-5] 
        httpLine = httpstatuscode + "\t\t| " + urlstatuscode
        lineashttp.append(httpLine)
    elif "Trace written by version" in linea:
        broker = (lineas_entrada[i+1])
        indexBroker = broker.find("Integration node :") + len("Integration node :")
        indexBroker2 = broker.find("; Integration server")
        broker = broker[indexBroker:indexBroker2]

        egName = (lineas_entrada[i+1])
        indexEg = egName.find("Integration server :") + len("Integration server :")
        indexEg2 = egName.find("; Trace type")
        egName = egName[indexEg:indexEg2]
    elif "The input node ''HTTP Input'' has received data and has propagated it to the message flow ''gen" in linea:
        apiName = (lineas_entrada[i])
        indexApi = apiName.find("gen.") + len("gen.")
        apiName = apiName[indexApi:-5]


print(errores)

with open('archivo_salida.txt', 'w') as archivo_salida:
    archivo_salida.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    archivo_salida.write('BROKER: '+broker+'|'+egName+'| '+apiName+' |\n')
    archivo_salida.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    archivo_salida.write('ERROR\t|\t\t\t\t\tCODIGO\t\t\t\t\t\t| MandatoryCoreId = '+ mandatoryCoreId +' |\n')
    archivo_salida.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    archivo_salida.write('\n'.join(lineas_salida))
    archivo_salida.write('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    archivo_salida.write('HTTP\t|\t\t\t\t\tENDPOINT')
    archivo_salida.write('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    archivo_salida.write('\n'.join(lineashttp))
