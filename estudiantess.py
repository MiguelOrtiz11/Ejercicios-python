def entrarNombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante a añadir: ")
        if nombre == "":
            print("El nombre no puede estar vacio")
        else:
            return nombre


def entrarNotas():
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0-10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("La nota no tiene que estar entre 0 y 10")
        except:
            print("La nota tiene que ser un valor numerico")


def devolverEstudiante():
    nombre = entrarNombre()
    for estu in estudiantes:
        if estu[0] == nombre:
            print("La nota del estudiante es '{}' es {}".format(
                nombre, estu[1]))
            return True
    print("No se encuentra el estudiante")
    return False


def modificarNota():
    nombre = entrarNombre()
    indice = buscarEstudiante(nombre)
    if indice == -1:
        print("No se ha encontrado el estudiante'{}'".format(nombre))
        return False
    else:
        tmp = (list(estudiantes[indice]))
        tmp[1] = entrarNotas()
        estudiantes[indice] = tuple(tmp)
        print("Se ha actualizado la nota del estudiante '{}'".format(nombre))
        return True


def buscarEstudiante(nombre):
    for i, e in enumerate(estudiantes):
        if e[0] == nombre:
            return i
    return -1


def listarEstudiantesNombre():
    estudiantes.sort()
    print("\n".join(i[0]+" - " + str(i[1])for i in estudiantes))
    return True

def menu():
    print("------------------------------")
    print("Seleccione una opción...")
    print("\t1 - Añadir estudiante")
    print("\t2 - Buscar estudiante")
    print("\t3 - Modificar nota")
    print("\t4 - Listado de estudiantes ordenados por el nombre")
    print("\t5 - Listado de estudiantes ordenados por su nota")
    print("\t6 - Mostrar la media de las notas")
    print("\t7 - Borrar estudiante")
    print("\n\t0 - Salir")


estudiantes = []
aux = True
while aux:
    menu()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1
    if opcion == 1:
        estudiantes.append((entrarNombre(), entrarNotas()))
    elif opcion == 2:
        devolverEstudiante()
    elif opcion == 3:
        modificarNota()
    elif opcion == 4:
        listarEstudiantesNombre()
    elif opcion == 0:
        aux = False
