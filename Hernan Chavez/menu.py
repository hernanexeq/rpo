from GestorMiembros import gestormiembros
from GestorVisualizaciones import gestorvisualizaciones
def menu(gm,gv):
    print("Elija una opcion\n")
    print("a. Ingresar el correo electrónico de un miembro e indicar la cantidad total de minutos que ha visto películas.")
    print("b. Mostrar apellido, nombre y correo electrónico de las miembros que han realizado visualizaciones simultáneas. ") 
    print("c. Salir\n")
    opcion=int(input("Ingrese una opcion: "))
    if opcion=='a':
        correo=str(input("Ingrese correo: "))
        id= gm.buscarmiembro(correo)
        a= gv.buscarid(id)
        print("La cantidad total de minutos visualizado es de: ",a)
    elif opcion=='b':
        gv.mostrarvsimul(gm)
    elif opcion=='c':
        print("Adios.")
    else:
        print("Opcion no valida.")