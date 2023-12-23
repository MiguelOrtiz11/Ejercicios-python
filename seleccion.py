#funciones
def leerlista():
    lista=[]
    cant=int(input("digite la cantidad de numeros a ingresar: "))
    for i in range(cant):
        lista.append(int(input("ingrese un numero ")))
    return lista
     
def seleccion(lista,tam):
    for i in range(0,tam-1):
        min=1
        for j in range(i+1,tam):
            if lista[min]>lista[j]:
                min=j
        aux=lista[min]
        lista[min]=lista[i]
        lista[i]=aux


def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])   

#cuerpo programa
a=leerlista()
print(a)
seleccion(a,len(a))
imprimirlista(a,len(a))
print(a)