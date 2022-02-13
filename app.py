from glob import glob
import imp
from math import fabs
from operator import le
from os import system
import os
import re
from tkinter import filedialog
import xml.etree.ElementTree as ET

#R es Filas
#C es Columnas
#F Costo de volteo en Quetzales
#S Costo de intercambio en Quetzales






def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def opciones():
    
    while True:
        print("***************************************************")
        print("*"+"           Pisos Artesanales, S.A"+ "                *")
        print("*"+" Hola, elijamos nuestro archivo de entrada"+ "       *")
        print("***************************************************")
        leerArchivo()

        

def leerArchivo():
    direcion = filedialog.askopenfilename(initialdir ='/', 
										title='Escoger Tu archivo de entrada', 
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    archivo_xml = ET.parse(direcion)
    root = archivo_xml
    return root


if __name__ == "__main__":
    
    clearConsole()
    opciones()