
class Lista:
    def __init__(self, valor= None, Siguiente= None):
        self.valor = valor
        self.Siguiente = Siguiente

class Lista_Nueva:
    def __init__(self, valor= None, Siguiente= None):
        self.valor = valor
        self.Siguiente = Siguiente

class Nodo_Nuevo:    
    def __init__(self):
        self.raiz_nueva = Lista_Nueva()
        self.ultimo_nueva = Lista_Nueva()
        self.raiz = Lista()
        self.ultimo = Lista()

    def insertar(self, nuevoNodo):
        if self.raiz_nueva.valor == None:
            self.raiz_nueva = nuevoNodo
            self.ultimo_nueva = nuevoNodo
        
        elif self.raiz_nueva.Siguiente == None:
            self.raiz_nueva.Siguiente = nuevoNodo
            self.ultimo_nueva = nuevoNodo
        else:
            self.ultimo_nueva.Siguiente = nuevoNodo
            self.ultimo_nueva = nuevoNodo

    def insertar_actual(self, nuevoNodo):
        if self.raiz.valor == None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        
        elif self.raiz.Siguiente == None:
            self.raiz.Siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.Siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def imprimirnombre(self,columnas):
        x = 0
        aux = self.raiz
        while True:
            if aux.valor == None:
                break
            else:
                if x == columnas:
                    x = 1
                    print("\n"+aux.valor, end="")
                    if aux.Siguiente == None:
                        break
                    else:    
                        aux = aux.Siguiente                    

                else:
                    print(aux.valor, end="")
                    x = x + 1
                    if aux.Siguiente == None:
                        break
                    else:    
                        aux = aux.Siguiente
        
        print("\n")


    def organizar_matriz(self,secuencia, nueva_secuencia, columnas ,volteos_precios, cambios_precios):
        #Totales
        volteos_totales =0
        cambios_totales =0
    
        

        for i in secuencia:
            
            self.insertar_actual(Lista(i))
    
        for i in nueva_secuencia:
            self.insertar(Lista_Nueva(i))

        aux_actual = self.raiz
        aux_nueva = self.raiz_nueva
        aux_columna = aux_actual.Siguiente
        aux_fila = None


        for i in range(columnas+1):
            if aux_actual.valor == None:
                aux_fila = None
                break
            else:
                aux_fila = aux_actual
                aux_actual = aux_actual.Siguiente
        aux_actual = self.raiz
        
        
        while True:
            
            try:
                if aux_actual.valor == None and aux_nueva.valor == None:                    
                    break
                else:
                    if aux_actual.valor == aux_nueva.valor:
                        if aux_actual.Siguiente == None:                            
                            break
                        else:    
                            print("No hay cambios ya que son iguales")
                            self.imprimirnombre(columnas)
                            aux_actual = aux_actual.Siguiente    
                            aux_nueva = aux_nueva.Siguiente
                            aux_columna = aux_actual.Siguiente
                            aux_fila = None
                            aux_rapida = aux_actual                           
                            
                            for i in range(columnas+1):
                                if aux_actual.Siguiente == None:
                                    aux_fila = None
                                    break
                                else:
                                    aux_fila = aux_actual
                                    aux_actual = aux_actual.Siguiente
                            aux_actual = aux_rapida

                    else:                        
                            print("No son iguales asi que se debe volver a organizar")

                            if aux_nueva.valor == aux_columna.valor:
                                print("Se ingreso en cambio a la izquierda")
                                aux_columna1 = aux_columna.Siguiente
                                aux_fila1 = aux_fila.Siguiente

                                if aux_columna.valor == aux_columna1.valor:
                                    cambios_totales += 1
                                    print("Cambio: ",aux_actual.valor, "->", aux_nueva.valor)
                                    aux_actual.Siguiente.valor = aux_actual.valor
                                    aux_actual.valor = aux_nueva.valor

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida
                                    
                                    aux_nueva = aux_rapida
                                    self.imprimirnombre(columnas)

                                elif aux_columna.valor == aux_fila1.valor:
                                    cambios_totales += 1
                                    print("Cambio: ",aux_actual.valor, "->", aux_nueva.valor)
                                    aux_actual.Siguiente.valor = aux_actual.valor
                                    aux_actual.valor = aux_nueva.valor

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida
                                    
                                    self.imprimirnombre(columnas)

                                else:
                                    volteos_totales += 1
                                    print("Volteo: ",aux_actual.valor, "->", aux_nueva.valor)                                    
                                    aux_actual.valor = aux_nueva.valor       

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida

                                    self.imprimirnombre(columnas)                                                          
                                    
                            elif aux_nueva.valor == aux_fila.valor:
                                aux_columna1 = aux_columna.Siguiente
                                aux_fila1 = aux_fila.Siguiente

                                if aux_actual.valor == aux_columna1.valor:
                                    cambios_totales += 1
                                    print("Cambio: ",aux_actual.valor, "->", aux_nueva.valor)
                                    aux_actual.Siguiente.valor = aux_actual.valor
                                    aux_actual.valor = aux_nueva.valor

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida
                                    
                                    self.imprimirnombre(columnas)

                                elif aux_actual.valor == aux_fila1.valor:
                                    cambios_totales += 1
                                    print("Cambio: ",aux_actual.valor, "->", aux_nueva.valor)
                                    aux_actual.Siguiente.valor = aux_actual.valor
                                    aux_actual.valor = aux_nueva.valor

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida
                                    
                                    self.imprimirnombre(columnas)

                                else:
                                    volteos_totales += 1
                                    print("Volteo obligado: ",aux_actual.valor, "->", aux_nueva.valor)                                    
                                    aux_actual.valor = aux_nueva.valor       

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida

                                    self.imprimirnombre(columnas)  

                            else:
                                    volteos_totales += 1
                                    print("Volteo: ",aux_actual.valor, "->", aux_nueva.valor)                                    
                                    aux_actual.valor = aux_nueva.valor       

                                    #Reinicio
                                    aux_actual = aux_actual.Siguiente    
                                    aux_nueva = aux_nueva.Siguiente
                                    aux_columna = aux_actual.Siguiente
                                    aux_fila = None
                                    aux_rapida = aux_actual                           
                            
                                    for i in range(columnas+1):
                                        if aux_actual.Siguiente == None:
                                            aux_fila = None
                                            break
                                        else:
                                            aux_fila = aux_actual
                                            aux_actual = aux_actual.Siguiente


                                    aux_actual = aux_rapida
                                    self.imprimirnombre(columnas)

            except: 
                volteos_totales += 1
                print("Volteo: ",aux_actual.valor, "->", aux_nueva.valor)                                    
                aux_actual.valor = aux_nueva.valor      
                self.imprimirnombre(columnas)  

        print("Volteos totales: ", volteos_totales)
        print("Cambios totales: ", cambios_totales)
        print("Costo total: ", ((volteos_totales*volteos_precios)+(cambios_totales*cambios_precios)))
        return (self.raiz)




