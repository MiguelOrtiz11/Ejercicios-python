#hacer una lista vacia que agregeue 5 notas de un estudiante, calcule la definitica e imprima
#si aprobo  o no aprobo la materia
notas=0
numero=0
suma=0
definitiva=0
lista=[]
for i in range(5):
    notas=float(input("digite sus notas: "))
    lista.append(notas)
    suma=suma+notas
print(lista)
definitiva=suma/len(lista)
print("la definitiva es: ", round(definitiva,1))
if definitiva>=3:
    print("Felicidades, aprobaste!!!")
else:
    print("no aprobaste wacho :c")


