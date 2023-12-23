def sumatoria(lista):
    suma=0
    for n in lista:
        suma=suma+n
    return suma

def numeromenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva 