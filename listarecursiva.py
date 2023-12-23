#funciones
def cabeza(lista):
    return lista[0]
def cola(lista):
    return lista[1:]

#calular el maximo de una lista
def maximo(lista):
    #caso base
    if (len(lista)==1):
        return cabeza(lista)
        #regal recursiva
    head=cabeza(lista)
    maximacola=maximo(cola(lista))
    return head if head>maximacola else maximacola

#calcular la sumatoria de una lista
def sumatoria(lista):
    #caso base
    if (len(lista)==0):
        return 0
    #regla recursiva
    return cabeza(lista)+sumatoria(cola(lista))

#reducir la lista
def reducir(lista,funcion):
    #caso base
    if(len(lista)==1):
        return lista[0]
    #regla recursiva
    return funcion(cabeza(lista), reducir(cola(lista),funcion))

#cuerpo del programa

#el numero maximo de la lista
print("el valor maximo de la lista es: ", maximo([1,2,3,4,5,234]))

#la sumatoria de la lista
print("la smatoria de la lista es: ", sumatoria([1,123,4,53,75,6856,8,9]))

#reducir la lista
print("la lista reducida es: ", reducir([1,12,312,4,536,7,123],lambda x,y:x+y))