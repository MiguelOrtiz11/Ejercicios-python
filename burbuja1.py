#funciones
def leerlista():
    lista=[]
    cant=int(input("digite la cantidad de numeros a ingresar: "))
    for i in range(cant):
        lista.append(int(input("ingrese un numero ")))
    return lista
       
def burbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
             if lista [j]>lista[j+1]:
                k=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=k
     
def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])   
#cuerpo programa
a=leerlista()
print(a)
burbuja(a,len(a))
print(a)
imprimirlista(a,len(a))