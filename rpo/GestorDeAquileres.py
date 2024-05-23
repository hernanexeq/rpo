import csv
import numpy as np
from Alquiler import alquiler
from GestorDeCanchas import gestordecanchas
class gestordealquileres():
    __lista=list
    def __init__(self):
        self.__lista=[]
    def __str__(self):
        s="Cliente Cancha Hora Minutos Duracion\n"
        for alquiler in self.__lista:
            s += str(alquiler) + '\n'
        return s
    def agregaralquiler(self,unalquiler):
        self.__lista.append(unalquiler)
    def testalquiler(self):
        archivo=open('Alquiler.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                nom= fila[0]
                id= fila[1]
                hs= fila[2]
                min= fila[3]
                dur= fila[4]
                unalquiler=alquiler(nom,id,hs,min,dur)
                self.agregaralquiler(unalquiler)
        archivo.close
    def ordenar(self):
        self.__lista.sort(key=lambda alquiler: alquiler.__hs )  
    def getalquiler(self,indice):
        return self.__lista[indice] 
    def mostrarformato(self,gc):
        self.ordenar()
        acum=0
        print("Hora  Id de Cancha  Duracion de Alquiler  Importe por Hora  Importe Alquiler")
        for i in range(len(self.__lista)):
            hs=self.formato(i)
            id=self.id(i)
            im=self.imp(i,gc)
            d= self.duracion(i)
            impal= float(d*im)
            acum+=impal
            print(hs,"  ",id,"  ",d,"  ",im,"  ",impal)
        print("Total recaudado: ",acum)
    def formato(self,i):
        hora= str(self.__lista[i].geths())+":"+str(self.__lista[i].getmin)
        print(hora)
    def duracion(self,i):
        dur= float((self.__lista[i].getDura())/60)
        return dur
    def id(self,i):
        ide= self.__lista[i].getid()
        return ide 
    def imp(self,id,gc):
        pos= gc.buscarimp(id)
        if pos!=-1:
            return pos
    def buscarid(self,id):
        acum=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getId()==id:
                acum+= int(self.__lista[i].getDura())
        return acum