import numpy as np
from Miembro import miembro
import csv
class gestormiembros:
    __cantidad= int
    __dimension= int
    __incremento= 10
    __arreglo= np.array
    def __init__(self,dimension=10):
        self.__arreglo=np.empty(dimension,dtype=miembro)
        self.__cantidad=0
    def agregarmiembro(self,unmiembro):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=unmiembro
        self.__cantidad+=1
    def testmiembro(self):
        archivo=open('Miembros.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                id= fila[0]
                apyn= fila[1]
                correo= fila[2]
                unmiembro=miembro(id,apyn,correo)
                self.agregarmiembro(unmiembro)
        archivo.close
    def buscarmiembro(self,correo):
        i=0
        id=-1
        while i<len(self.__arreglo) and self.__arreglo[i].getcorreo()!=correo:
            i+=1
        if i<len(self.__arreglo):
            id= self.__arreglo[i].getid()
        return id
    def buscarid(self,id):
        i=0
        posicion=-1
        while i<len(self.__arreglo) and self.__arreglo[i].getid()!=id:
            i+=1
        if i<len(self.__arreglo):
            posicion=i
        return posicion
    def mostrardatos(self,i):
        if i!=-1:
            print(self.__arreglo[i].getayn()," ",self.__arreglo[i].getcorreo())