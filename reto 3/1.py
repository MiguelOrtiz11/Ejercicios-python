numeros=[]
num=int(input("digite un numero: "))
while num>= 0:
   numeros.append(num)
   print(numeros)
   num=int(input("digite un numero: "))
print(numeros)

def extraerpares(lista):
    pares=[]

    for n in lista:
        if n%2==0:
            pares.append(n)

    return pares

print()

resultado = extraerpares(numeros)

print("contenido de los numeros pares de la tabla", resultado)





