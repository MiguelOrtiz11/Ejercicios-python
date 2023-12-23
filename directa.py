def leerLista():
    lista=[]
    cant=int(input("digite la cantidad de numeros a ingresar: "))
    for i in range(0,cant):
        lista.append(int(input("ingrese un numero: ")))
    return lista

def insercciondirecta(lista,tam):
    for i in range(1,tam):
        v=lista[i]
        j=i-1
        while j>=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=v

def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])

a=leerLista()
print(a)
insercciondirecta(a,len(a))
imprimirlista(a,len(a))
print(a)
