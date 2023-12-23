lista=[]
lista.append([2,4,5])
lista.append([6,23,34])
print(lista)

lista2=[]
dato=0
for i in range(2):
    lista2.append([])
    for j in range(3):
        dato=dato+2
        lista2[i].append(dato)
print(lista2)



lista2=[]
for i in range(2):
    lista2.append([])
    for j in range(3):
        dato=input("digite un dato")
        lista2[i].append(dato)
print(lista2)