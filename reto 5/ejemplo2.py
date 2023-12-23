#funciones

def rival():
    while True:
        nombrerival = input("digite el nomrbe del equipo rival: ")
        if nombrerival=="":
            print("debe agregar un nombre")
        else:
            return nombrerival

def fecha():
    dia=input("digite dia: ")
    mes=input(" digite mes: ")
    anio=input("digite anio: ")
    print(dia, mes, anio)

#def golesuma():
 







#def registro():

def menu():
    print("------------------------------")
    print("Seleccione una opción...")
    print("\t1 - registrar partido")
    print("\t2 - ver resultados")
    print("\t3 - tabla de clasificacion")
    print("\n\t0 - salir")

#cuerpo del programa
dato = []
aux = True
while aux:
    menu()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1
    if opcion == 1:
        dato.append(rival())
    if opcion == 2:
        dato.append(fecha())
        