#hacer un programa que cree una lista vacia, en la cual vamos a agregar 10 posiciones, para
#digitar unos numeros, los cuales se deben sumar y obtener el promedio
lista=[]
suma=0
promedio=0
numero=0
for i in range(10):
    numero=int(input("digite un numero: "))
    lista.append(numero)
    suma=suma+numero
print(lista)
promedio=suma/len(lista)
print("la suma es: ", suma)
print("el promedio es: ", promedio)
print("fin del programa")
