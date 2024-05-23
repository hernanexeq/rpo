from GestorDeAquileres import gestordealquileres
from GestorDeCanchas import gestordecanchas
from menu import menu
if __name__=='__main__':
    ga=gestordealquileres()
    gc=gestordecanchas()
    ga.testalquiler()
    gc.testcancha()
    menu(gc,ga)