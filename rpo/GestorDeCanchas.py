import numpy as np
from Cancha import cancha
import csv
class gestordecanchas:
    __cantidad=int
    __dimension=6
    __incremento=3
    __canchas=np.array
    def __init__(self):
        self.__canchas=np.empty(self.__dimension,dtype=cancha)
        self.__cantidad=0
    def agregarcancha(self,unacancha):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__canchas.resize(self.__dimension)
        self.__canchas[self.__cantidad]=unacancha
        self.__cantidad+=1
    def testcancha(self):
        archivo=open('Canchas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                id= fila[0]
                tipo= fila[1]
                imp= fila[2]
                unacancha=cancha(id,tipo,imp)
                self.agregarcancha(unacancha)
        archivo.close
    def getcancha(self,indice):
        return self.__canchas[indice]
    def buscarimp(self,id):
        i=0
        posicion=-1
        while i<len(self.__canchas) and self.__canchas[i].getid()!=id:
            i+=1
        if i<=len(self.__canchas):
            posicion=i
        return posicion