#funciones
def leerlista():
    lista=[]
    cant=int(input("digite la cantidad de numeros a ingresar: "))
    for i in range(cant):
        lista.append(int(input("ingrese un numero ")))
    return lista
    
def quicksort(lista,izq,der):
    i=izq
    j=der
    x=lista[(izq+der)//2]

    while(i<=j):
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
            i=i+1
            j=j-1
        if izq<j:
            quicksort(lista,izq,j)
    if i<der:
        quicksort(lista,i,der)

def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])   

#cuerpo programa
a=leerlista()
print(a)
quicksort(a,0,len(a)-1)
imprimirlista(a,len(a))
print(a)