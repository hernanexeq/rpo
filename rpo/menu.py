from GestorDeAquileres import gestordealquileres
from GestorDeCanchas import gestordecanchas
def menu(gc,ga):
    print("Elija una opcion")
    print("1. Emitir un listado ordenado por hora y minutos con todos los alquileres registrados\n")
    print("2. Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo alquilada.\n")
    print("3. Salir\n")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        ga.mostrarformato(gc)
    elif opcion==2:
        id=str(input("Ingrese id de la cancha: "))
        print("Total de minutos alquilada: ",ga.buscarid(id))
    elif opcion==3:
        print("Adios.")
    else:
        print("Opcion no valida.")