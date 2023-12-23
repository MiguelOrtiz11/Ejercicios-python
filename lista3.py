#solicitar al usuario que ingrese numeros, los cuales se gaurdaran en una lista
#finalizar al ingresar el numero 0, el cual no debe guardarse

from funciones import numeromenores, sumatoria


numeros=[]
num=int(input("digite un numero: "))
while num!=0:
    numeros.append(num)
    print(numeros)
    num=int(input("digite un numero: "))
print(numeros)
print("fin del programa")

#a continuacion, solicitar al usuario que ingrese un numero y si el numero esta en la lista 
#eliminar su primera ocurrencia, mostrar un mensaje si no es posible eliminarlo

eliminar=int(input("digite el numero a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("este numero no esta en la lista!")
print(numeros)
print("fin :D")

#imprimir la sumatoria de todos los numeros de la lista
print("la sumatoria de la lista es: ", sumatoria(numeros))

#solicitar al usuario otro numero y crear una lista con los elementos de la lista original
#menores que el numero dado. imprimir esta nueva lista

limite=int(input("filtrar numeros menores a: "))
for n in numeromenores(numeros, limite):
    print(n)

    