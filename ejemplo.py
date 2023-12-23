numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)


    numeros=[]
num=int(input("digite un numero: "))
while num>= 0:
   numeros.append(num)
   print(numeros)
   num=int(input("digite un numero: "))
print(numeros)
print("fin del programa")