#hacer un programa que pida un numero por teclado y guardar en una lista
#su tabla de multiplicar
numero=int(input("digite un numero: "))
lista=[]
for i in range(1,11):
    lista.append(i*numero)
print(lista)
print("fin del programa")

