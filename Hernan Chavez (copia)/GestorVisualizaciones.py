from Visualizacion import visualizacion
from GestorMiembros import gestormiembros
import csv
class gestorvisualizaciones:
    __lista=list
    def __init__(self):
        self.__lista=[]
    def agregarvisualizacion(self,unavisualizacion):
        self.__lista.append(unavisualizacion)
    def testvisualizacion(self):
        archivo=open('Visualizaciones.csv')
        reader= csv.reader(archivo,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                id= fila[0]
                idpel= fila[1]
                f= fila[2]
                hs= fila[3]
                min= fila[4]
                unavis= visualizacion(id,idpel,f,hs,min)
                self.agregarvisualizacion(unavis)
        archivo.close
    def buscarid(self,id):
        acum=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getid()==id:
                acum+= self.__lista[i].getmin()
        return acum
    """def mostrarvsimul(self,gm):
        a: visualizacion
        for i in range(len(self.__lista)):
            a=self.__lista[i]
            j=i+1
            for j in range(len(self.__lista)):
                if self.__lista[j].__eq__(a):
                    pos= gm.buscarid(self.__lista[j].getid())
                    gm.mostrardatos(pos)"""
    def mostrarvsimul(self,gm):
        a: visualizacion
        i=0
        j=1
        while i<len(self.__lista):
            a=self.__lista[i]
            while j<len(self.__lista):
                if self.__lista[j].__eq__(a):
                    pos= gm.buscarid(self.__lista[j].getid())
                    gm.mostrardatos(pos)
                j+=1
            i+=1
        
