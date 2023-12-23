def entrarNombre():
    while True:
        nombre = input("Ingrese el nombre del producto a añadir: ")
        if nombre == "":
            print("El nombre no puede estar vacio")
        else:
            return nombre


def entrarCompras():
    while True:
        try:
            compra = float(input("Ingrese valor del producto: "))
            if 0 <= compra:
                return compra
            else:
                print("La nota no tiene que estar en 0")
        except:
            print("La nota tiene que ser un valor numerico")


def devolverProducto():
    nombre = entrarNombre()
    for pro in producto:
        if pro[0] == nombre:
            print("el valor del producto '{}' es {}".format(
                nombre, pro[1]))
            return True
    print("No se encuentra el producto")
    return False


def modificarCompra():
    nombre = entrarNombre()
    indice = buscarProducto(nombre)
    if indice == -1:
        print("No se ha encontrado el producto'{}'".format(nombre))
        return False
    else:
        tmp = (list(producto[indice]))
        tmp[1] = entrarCompras()
        producto[indice] = tuple(tmp)
        print("Se ha actualizado el valor de compra del producto '{}'".format(nombre))
        return True


def buscarProducto(nombre):
    for i, e in enumerate(producto):
        if e[0] == nombre:
            return i
    return -1


def listarProductoNombre():
    producto.sort()
    print("\n".join(i[0]+" - " + str(i[1])for i in producto))
    return True

def listarProductoCompra():
    producto.sort(key=lambda x: x[1], reverse=True)
    print("\n". join(i[0]+" - "+str(i[1]) for i in producto))
    return True

def notapromedio():
    if len(producto)==0:
        print("no hay producto")
        return False
    promedio=sum([i[1]for i in producto])/len(producto)
    print("el valor de compra promedio de los", len(producto), "productos es '{}'".format(promedio))

def borrarProducto():
    nombre = entrarNombre()
    indice = buscarProducto(nombre)
    if indice == -1:
        print("No se ha encontrado el producto'{}'".format(nombre))
        return False
    print("se ha eliminado el producto '{}' con valor de compra {}".format(nombre,producto[indice][1]))
    del producto[indice]
    return True


def menu():
    print("------------------------------")
    print("Seleccione una opción...")
    print("\t1 - Añadir producto")
    print("\t2 - Buscar producto")
    print("\t3 - Modificar compra")
    print("\t4 - Listado de productos ordenados por el nombre")
    print("\t5 - Listado de productos ordenado por el valor de la compra")
    print("\t6 - Mostrar la media del valor de compra")
    print("\t7 - Borrar producto")
    print("\n\t0 - Salir")


producto = []
aux = True
while aux:
    menu()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1
    if opcion == 1:
        producto.append((entrarNombre(), entrarCompras()))
    elif opcion == 2:
        devolverProducto()
    elif opcion == 3:
        modificarCompra()
    elif opcion == 4:
        listarProductoNombre()
    elif opcion==5:
        listarProductoCompra()
    elif opcion==6:
        notapromedio()
    elif opcion==7:
        borrarProducto()
    elif opcion==0:
        break
    else:
        print("la opcion ingresada no es la correcta, indica una opcion correcta mamahuevo")

