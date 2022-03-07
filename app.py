import os
import sys
from tkinter import filedialog
from tkinter.messagebox import NO
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph
from algoritmo import Nodo_Nuevo


#R es Filas
#C es Columnas
#F Costo de volteo en Quetzales
#S Costo de intercambio en Quetzales


class Nodo:
    def __init__(self,nombre = None, fila = None, columna = None, costo_volteo = None, costo_intercambio = None, siguiente = None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.costo_volteo = costo_volteo
        self.costo_intercambio = costo_intercambio
        self.siguiente = siguiente


class codigos:
    def __init__(self, codigo = None, nombre = None,nombre_pertenece = None, siguiente = None):
        self.codigo = codigo
        self.nombre = nombre
        self.nombre_pertenece = nombre_pertenece
        self.siguiente = siguiente
        
class Lista_piso:
    def __init__(self):
        self.raiz = codigos()
        self.ultimo = codigos()

    def insertar_piso(self, nuevocodigo):
        if self.raiz.nombre == None:
            self.raiz = nuevocodigo
            self.ultimo = nuevocodigo
        
        elif self.raiz.siguiente == None:
            self.raiz.siguiente = nuevocodigo
            self.ultimo = nuevocodigo
        
        else:
            self.ultimo.siguiente = nuevocodigo
            self.ultimo = nuevocodigo        

    def buscar_piso(self, nombre):
        global palabra
        palabra = ""
        if self.raiz.nombre == None:
            return None
        else:
            aux = self.raiz
            while aux != None:
                if aux.nombre == nombre:
                    for i in aux.codigo:
                        if i == "W" or i == "B":
                            palabra += i
                            
                    break
                else:
                    aux = aux.siguiente
            return aux

    def intercambiar_piso(self, nombre, nuevo_codigo):
        if self.raiz.nombre == None:
            return None
        else:
            aux = self.raiz

            while self.raiz != None:
                if self.raiz.nombre == nombre:
                    self.raiz.codigo = nuevo_codigo   

                self.raiz = self.raiz.siguiente
            
            self.raiz = aux
            return self.raiz

        
        

    def imprimir_piso(self, nombre):
        if self.raiz.nombre == None:
            print("No hay pisos")
        else:
            aux = self.raiz
            while aux != None:
                if aux.nombre_pertenece == nombre:
                    print("Nombre: ", aux.nombre)
                    aux = aux.siguiente
                else:
                    aux = aux.siguiente

    def imprimir_todo(self):
        if self.raiz.nombre == None:
            print("No hay pisos")
        else:
            aux = self.raiz
            while aux != None:
                print("Código: ", aux.nombre)
                aux = aux.siguiente

    def eliminar_piso(self, nombre):
        if self.raiz.nombre == None:
            return None
        else:
            aux = self.raiz
            while aux != None:
                if aux.nombre == nombre:
                    if aux.siguiente == None:
                        self.raiz = None
                        break
                    else:
                        aux.siguiente = aux.siguiente.siguiente
                        break

                aux = aux.siguiente
            return self.raiz


    #ordenar en alfabetico
    def ordenar_piso(self):
        if self.raiz.nombre == None:
            return None
        else:
            aux = self.raiz
            while True:
                if aux.siguiente != None:
                    if aux.nombre > aux.siguiente.nombre:
                        aux.nombre, aux.siguiente.nombre = aux.siguiente.nombre, aux.nombre
                        aux = aux.siguiente

                    else:
                        aux = aux.siguiente

                else:
                    break


class ListaSimple_Nodo:
    def __init__(self):
        self.raiz = Nodo()
        self.ultimo = Nodo()

    def insertar(self, nuevoNodo):
        if self.raiz.fila == None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        
        elif self.raiz.siguiente == None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def imprimirnombre(self):
        aux = self.raiz
        while True:
            if aux.fila == None:
                break
            else:
                print("Nombre: ",aux.nombre)
                if aux.siguiente == None:
                    break
                else:    
                    aux = aux.siguiente

    def buscarpatron(self, patron):
        aux = self.raiz
        while True:
            if aux.fila == None:
                break
            else:
                if aux.nombre == patron:
                    return aux
                else:
                    if aux.siguiente == None:
                        break
                    else:
                        aux = aux.siguiente

    def eliminar(self, nombre):
        if self.raiz.fila == None:
            return None
        else:
            aux = self.raiz

            while self.raiz != None:

                if self.raiz.nombre == nombre:
                    if self.raiz.siguiente == None:
                        self.raiz = None
                        break
                    else:
                        self.raiz = self.raiz.siguiente
                        break
                else:
                    self.raiz = self.raiz.siguiente

            self.raiz = aux
            return self.raiz

    
    def ordenar(self):
        if self.raiz.fila == None:
            return None
        else:
            aux = self.raiz
            while True:
                if aux.siguiente != None:
                    if aux.nombre > aux.siguiente.nombre:
                        aux.nombre, aux.siguiente.nombre = aux.siguiente.nombre, aux.nombre
                        aux = aux.siguiente
                    else:
                        aux = aux.siguiente
                else:
                    break

 

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def menu():
    global nuevalista, nuevopatron, palabra
    #clearConsole()
    print("***************************************************")
    print("*"+"           ¿Qué deseas hacer? "+"                  *")
    print("*"+" 1. Mostrar graficamente un patron "+"               *")
    print("*"+" 2. Cambiar un tipo de piso "+"                      *")
    print("*"+" 3. Mostrar todos los pisos cargados "+"             *")
    print("*"+" 4. Salir "+"                                        *")
    print("***************************************************")
    opcion = int(input("Ingrese una opcion: "))


    if opcion == 1:
        
        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Hola, elijamos nuestro patron"+ "       *")
        print("*"+" Nuestros Nombres de pisos disponibles son: "+ "       *")
        nuevalista.imprimirnombre()
        print("***************************************************")
        patron = input("Ingrese el nombre del piso que desea buscar: ")
        
        patron_encontrado = nuevalista.buscarpatron(patron)
        if patron_encontrado == None:
            print("*"+" No se encontró el nombre ingresado"+"       *")
            menu()
    

        else:
            print("*"+" Nuestros códigos disponibles son: "+ "       *")
            nuevopatron.imprimir_piso(patron_encontrado.nombre)
            codigo = input("Ingrese codigo de patron que desea aplicar: ")
        
        
            if patron_encontrado == None:
                print("No se encontro el patron")
            else:
                print("Imprimiendo patron: ", patron_encontrado.nombre)
                graphviz(patron_encontrado.nombre,codigo)

    elif opcion == 2:

        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Hola, elijamos nuestro patron"+ "       *")
        print("*"+" Nuestros Nombres de pisos disponibles son: "+ "       *")
        nuevalista.imprimirnombre()
        print("***************************************************")
        patron = input("Ingrese el nombre del piso que desea buscar: ")
        
        patron_encontrado = nuevalista.buscarpatron(patron)
        if patron_encontrado == None:
            print("*"+" No se encontró el nombre ingresado"+"       *")
            menu()
    

        else:
            print("*"+" Nuestros códigos disponibles son: "+ "       *")
            nuevopatron.imprimir_piso(patron_encontrado.nombre)
            patron_actual = input("Ingrese codigo de patron que desea editar: ")      
            codigo_piso = nuevopatron.buscar_piso(patron_actual)        
            if codigo_piso == None:
                print("No se encontro el patron")
                menu()
            else:                             
                nuevo_patron = input("Ingrese su nuevo patron: ")
                a = Nodo_Nuevo()
                col = patron_encontrado.columna
                Aux_cambio = a.organizar_matriz(str(palabra),str(nuevo_patron),int(col),int(patron_encontrado.costo_intercambio),int(patron_encontrado.costo_volteo))
                nueva_secuencia = ""
                while True:
                    if Aux_cambio.Siguiente == None:
                        nueva_secuencia = nueva_secuencia + Aux_cambio.valor                        
                        break
                    else:
                        nueva_secuencia = nueva_secuencia + Aux_cambio.valor
                        Aux_cambio = Aux_cambio.Siguiente

                print("Nueva secuencia: ",nueva_secuencia)
                nuevopatron.intercambiar_piso(patron_actual,nueva_secuencia)
                menu()
                

        
    elif opcion == 3:
        nuevopatron.ordenar_piso()
        nuevalista.ordenar()
        
        nuevopatron.imprimir_todo()
        nuevalista.imprimirnombre()
        menu()

    elif opcion == 4:
        #cerrar programa
        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Gracias por utilizar nuestro servicio"+ "       *")
        print("***************************************************")
        sys.exit()

    else:
        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Opcion no valida"+ "       *")
        print("***************************************************")
        menu()
    

def opciones():
    global nuevalista, nuevopatron

    print("***************************************************")
    print("*"+"           Pisos Artesanales, S.A"+ "                *")
    print("*"+" Hola, elijamos nuestro archivo de entrada"+ "       *")
    print("***************************************************")
    leerArchivo()
    menu()
    
   
def graphviz(patron, secuencia):

    patron_encontrado = nuevalista.buscarpatron(patron)
    codigo_piso = nuevopatron.buscar_piso(secuencia)
    z = 0
    x = ""
    tr_inicio = '''<TR>'''
    tr_fin = '''</TR>'''
    cuerpo = ""


    dot = Digraph(filename='Grafica de pisos', format= 'png')
       
    z = int(patron_encontrado.columna)
    w = 0
    print("z: ", z)

    for i in codigo_piso.codigo:
            if i == "W":
                x = x+'''<TD BGCOLOR="white"><FONT >W</FONT></TD>'''
                w = w + 1
                if w == z:
                    cuerpo = cuerpo +tr_inicio+x+tr_fin
                    x = ""
                    w = 0
            elif i == "B":
                x = x+'''<TD BGCOLOR="black"><FONT COLOR="white">B</FONT></TD>'''
                w = w + 1
                if w == z:
                    cuerpo = cuerpo +tr_inicio+x+tr_fin
                    x = ""
                    w = 0
            else:
                None

    dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
			
            '''+cuerpo+'''

    </TABLE>>''')

            #generar salto de linea

            
    dot.view()
    menu()



def leerArchivo():
    global nuevalista, nuevopatron
    direcion = filedialog.askopenfilename(initialdir ='/', 
										title='Escoger Tu archivo de entrada', 
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    archivo_xml = ET.parse(direcion)
    xml_data = archivo_xml.getroot()
    lst_data = xml_data.findall('piso')
    nuevalista = ListaSimple_Nodo()
    nuevopatron = Lista_piso()
    for piso in lst_data:
        
        
        nombre = piso.attrib['nombre']
        filas= piso.find('R').text
        columnas= piso.find('C').text
        costo_volteo = piso.find('F').text
        costo_intercambio = piso.find('S').text
        patron = piso.find('patrones')
        patron_piso = ""
        nombre_patron = ""
        
        for patrones in patron:
            patron_piso = patrones.text
            nombre_patron = patrones.attrib['codigo']
            guardar_patron = codigos(patron_piso,nombre_patron, nombre)
            nuevopatron.insertar_piso(guardar_patron)

        nodo = Nodo(nombre, filas, columnas, costo_volteo, costo_intercambio)
        nuevalista.insertar(nodo)

if __name__ == "__main__":
    
    
    opciones()
