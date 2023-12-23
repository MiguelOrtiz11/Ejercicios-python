#hacer un programa que pida una cadena por teclado, agregar los caracteres en una lista sin espacios
cadena=input("digite una cadena por caracteres: ")
print(cadena)
lista=[]
for c in cadena: 
    if(c!=' '):
        lista.append(c)
print(lista)
print("fin del programa")