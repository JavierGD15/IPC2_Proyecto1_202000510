import imp
import os
from tkinter import filedialog
from tkinter.messagebox import NO
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph


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
        if self.raiz.nombre == None:
            return None
        else:
            aux = self.raiz
            while aux != None:
                if aux.nombre == nombre:
                    return aux
                else:
                    aux = aux.siguiente
            return None




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

    def imprimir(self):
        aux = self.raiz
        while True:
            if aux.fila == None:
                break
            else:
                print("Fila: ",aux.fila, "Columna: ", aux.columna, "Costo de volteo: ", aux.costo_volteo, "Costo de intercambio: ", aux.costo_intercambio)
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

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def opciones():
    global nuevalista, nuevopatron

    print("***************************************************")
    print("*"+"           Pisos Artesanales, S.A"+ "                *")
    print("*"+" Hola, elijamos nuestro archivo de entrada"+ "       *")
    print("***************************************************")
    leerArchivo()

    
    print("*"+"           ¿Qué deseas hacer? "+"                  *")
    print("*"+"1. Mostrar graficamente un patron "+"               *")
    print("*"+"2. Cambiar un tipo de piso "+"                      *")
    print("*"+"3. Mostrar todos los pisos cargados "+"             *")
    print("***************************************************")
    opcion = int(input("Ingrese una opcion: "))


    if opcion == 1:
        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Hola, elijamos nuestro patron"+ "       *")
        print("***************************************************")
        patron = input("Ingrese el nombre del piso que desea buscar: ")
        codigo = input("Ingrese codigo de patron que desea aplicar: ")
        patron_encontrado = nuevalista.buscarpatron(patron)
        
        if patron_encontrado == None:
            print("No se encontro el patron")
        else:
            print("Imprimiendo patron: ", patron_encontrado.nombre)
            graphviz(patron_encontrado.nombre,codigo)
    



        
def graphviz(patron, secuencia):

    patron_encontrado = nuevalista.buscarpatron(patron)
    codigo_piso = nuevopatron.buscar_piso(secuencia)
    x = 1
    datos = 0


    dot = Digraph(filename='Grafica de pisos', format= 'png')
    
    for i in patron_encontrado.fila:
        print(i)
        for j in codigo_piso.codigo:
            
            
            if j == "W":
                dot.node(str(x),shape = 'box', style = 'filled', fillcolor = 'white')
                x = x + 1
            elif j == "B":
                dot.node(str(x),shape = 'box', style = 'filled', fillcolor = 'black')
                x = x + 1
            else:
                None
            
            #generar salto de linea

            
    dot.view()


    



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
    
    clearConsole()
    opciones()
