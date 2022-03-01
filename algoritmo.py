secuencia ="WBBBB"
nueva_secuencia ="BBBWW"
filas = 1
columnas = 5

matriz = []
matriz2 = []
costos_matriz = []

#Variables para conocer los valores 
blanco_actual = 0
negro_actual = 0

blanco_nuevo = 0
negro_nuevo = 0

#Variable de cambios encontrados obligatorios
cambios = 0

#Totales
volteos_totales =0
cambios_totales =0
volteos_precios =1000
cambios_precios =1

total =""

def imprimir_matriz():
    u = 0
    print("***************************************************")
    for i in range(len(matriz)):
        if u == columnas:
            u = 1
            print("\n"+matriz[i], end="")
                

        else:
            print(matriz[i], end="")
            u = u+1
    print("\n")
    print("***************************************************")

    u = 0
    for i in range(len(matriz2)):
        if u == columnas:
            u = 1
            print("\n"+matriz2[i], end="")

        else:
            print(matriz2[i], end="")
            u = u+1
    print("\n")
    print("***************************************************")


for i in secuencia:
    if i == "W":
        blanco_actual= blanco_actual+1
    else:
        negro_actual = negro_actual+1

for i in nueva_secuencia:
    if i == "W":
        blanco_nuevo= blanco_nuevo+1
    else:
        negro_nuevo = negro_nuevo+1

if blanco_nuevo > blanco_actual:
    cambios = int(blanco_nuevo-blanco_actual)

elif blanco_nuevo == blanco_actual:
    cambios = 0

else:
    cambios = int(blanco_actual-blanco_nuevo)



aux =[]
for i in secuencia:
    aux.append(i)

for i in secuencia:
    
        matriz.append(i)
    

for i in nueva_secuencia:
    
        matriz2.append(i)
        
imprimir_matriz()
#iniciamos los costos

x = 0
y = 0
nuevo = ""


for i in range(len(matriz)):    
        if matriz[i] == matriz2[i]:
            continue
        else:
            #evaluamos el cambio
            try:
                if matriz2[i] == matriz[i+1]:
                    print("Entra en cambio de columna")
                    try:
                        if matriz[i] == matriz[i+2]:
                            
                            cambios_totales = cambios_totales+1
                            matriz[i+1] = matriz[i]
                            matriz[i] = matriz2[i]
                            print("cambio3333")
                            imprimir_matriz()                                                    
                            continue
                
                        elif matriz[i] == matriz[i+columnas]:
                            cambios_totales = cambios_totales+1
                            matriz[i+1] = matriz[i]
                            matriz[i] = matriz2[i]
                            print("cambio555")
                            imprimir_matriz()
                            continue

                        else:
                            cambios_totales = cambios_totales+1
                            matriz[i+columnas] = matriz[i]
                            matriz[i] = matriz2[i]
                            print("cambio1")
                            imprimir_matriz()
                            continue
                    except:
                            cambios_totales = cambios_totales+1
                            matriz[i+1] = matriz[i]
                            matriz[i] = matriz2[i]
                            print("cambio errrrror")
                            imprimir_matriz()                                                    
                            continue
                
                


                elif matriz2[i] == matriz[i+columnas]:
                    print("Entra en cambio de fila")
                    if matriz[i] == matriz[i+columnas+1]:
                        cambios_totales = cambios_totales+1
                        matriz[i+columnas] = matriz[i]
                        matriz[i] = matriz2[i]
                        print("cambio1")
                        imprimir_matriz()
                        continue
                
                    elif matriz[i] == matriz[i+columnas+columnas]:
                        cambios_totales = cambios_totales+1
                        matriz[i+columnas] = matriz[i]
                        matriz[i] = matriz2[i]
                        print("cambio1")
                        imprimir_matriz()
                        continue

                    else:
                        cambios_totales = cambios_totales+1
                        matriz[i+columnas] = matriz[i]
                        matriz[i] = matriz2[i]
                        print("cambio1")
                        imprimir_matriz()    
                        continue

                else:
                    print("Entra en volteo")
                    volteos_totales = volteos_totales+1
                    matriz[i] = matriz2[i]
                    imprimir_matriz()
                    continue
        
            except:
                volteos_totales = volteos_totales+1
                matriz[i] = matriz2[i]
                print("volteo por error total")
                imprimir_matriz()
                continue     

print("Volteos totales: ", volteos_totales)
print("Cambios totales: ", cambios_totales)
print("Costo total: ", ((volteos_totales*volteos_precios)+(cambios_totales*cambios_precios)))




