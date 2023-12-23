#hacer un programa que pida por teclado una cadena, agregue los caracteres en una lista s
#sin repetir caracteres
cadena=input("digite una cadena de caracteres: ")
print(cadena)
lista=[]
for c in cadena:
    if c not in lista:
        lista.append(c)
print(lista)
print("fin del programa")