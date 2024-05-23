from GestorMiembros import gestormiembros
from GestorVisualizaciones import gestorvisualizaciones
from menu import menu
if __name__=='__main__':
    gm=gestormiembros(18)
    gv=gestorvisualizaciones()
    gm.testmiembro()
    gv.testvisualizacion()
    menu(gm,gv)