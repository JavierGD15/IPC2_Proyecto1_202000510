
secuencia ="WBBBWBWWW"
nueva_secuencia ="WWWWBWWWB"
filas = 3
columnas = 3
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

total =""

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

print("Cambios: ", cambios)
volteos_totales = int(cambios)

aux =[]
for i in secuencia:
    aux.append(i)

#agregamos los cambios obligatorios
x=0
print("Aux inicial: ", aux)
if cambios > 0:
    for i in nueva_secuencia:
        if cambios == 0:
            break
        if aux[x] == i:
            x = x+1            
        else:
            aux[x] = i
            x = x+1
            cambios = cambios-1

    secuencia = ""
    #agregamos los cambios opcionales
    for i in aux:
        secuencia = secuencia + i        


#agregamos la matriz partida en niveles
for i in secuencia:
    
        matriz.append(i)

    

for i in nueva_secuencia:
    
        matriz2.append(i)
        

#iniciamos los costos

x = 0
y = 0
nuevo = ""
for i in range(len(matriz)):    
        if matriz[i] == matriz2[i]:
            continue

        else:
            #evaluamos el cambio
            if matriz2[i] == matriz[i+1]:
                cambios_totales = cambios_totales+1
                matriz[i+1] = matriz[i]
                matriz[i] = matriz2[i]   
                print("Matriz: ", matriz)
                print("Matriz2: ", matriz2)             
                continue
                
            elif matriz2[i] == matriz[i+columnas]:
                cambios_totales = cambios_totales+1
                matriz[i+columnas] = matriz[i]
                matriz[i] = matriz2[i]
                print("Matriz: ", matriz)
                print("Matriz2: ", matriz2)

            else:
                volteos_totales = volteos_totales+1
                matriz[i] = matriz2[i]
                print("Matriz: ", matriz)
                print("Matriz2: ", matriz2)
                    

print("Volteos totales: ", volteos_totales)
print("Cambios totales: ", cambios_totales)




