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
                fyh= fila[2]
                min= fila[3]
                unavis= visualizacion(id,idpel,fyh,min)
                self.agregarvisualizacion(unavis)
        archivo.close
    def buscarid(self,id):
        acum=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getid()==id:
                acum+= self.__lista[i].getmin()
        return acum
    def mostrarvsimul(self,gm):
        for i in range(len(self.__lista)):
            a=self.__lista[i]
            for j in range(len(self.__lista)):
                if self.__lista[j+1].__eq__(a):
                    pos= gm.buscarid(self.__lista[j+1].getid())
                    gm.mostrardatos(pos)