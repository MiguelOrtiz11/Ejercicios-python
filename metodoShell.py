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
     
def metodoshell(lista,tam):
    inc=1
    for inc in range(1,tam,inc*3+1):
        while inc>0:
            for i in range(inc,tam):
                j=i
                temp=lista[i]
                while j>=inc and lista[j-inc]>temp:
                    lista[j]=lista[j-inc]
                    j=j-inc
                lista[j]=temp
            inc=int(inc/2)

def imprimirlista(lista,tam):
    for i in range(tam):
        print(lista[i])   

#cuerpo programa
a=leerlista()
print(a)
metodoshell(a,len(a))
imprimirlista(a,len(a))
print(a)