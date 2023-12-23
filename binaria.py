#funciones
def leerlista():
    lista=[]
    cant=int(input("digite la cantidad de numeros a ingresar: "))
    for i in range(cant):
        lista.append(int(input("ingrese un numero ")))
    return lista
     
def inserccionbinaria(lista,tam):
    for i in range(1,tam):
        aux=lista[i]
        izq=0
        der=i-1
        while izq<=der:
            m=(izq+der)//2
            if aux<lista[m]:
                der=m-1
            else:
                izq=m+1
        j=i+1
        while j>izq:
            lista[j+1]=lista[j]
            j=j-1
        lista[izq]=aux


def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])   

#cuerpo programa
a=leerlista()
print(a)
inserccionbinaria(a,len(a))
imprimirlista(a,len(a))
print(a)