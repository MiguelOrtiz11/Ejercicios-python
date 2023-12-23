valor=['python' for i in range(3)]
print(valor)


print([i for i in range(6)])


cadena=input("digite dos numeros separados por coma")
dimension=[int(x) for x in cadena.split(',')]
numfila=dimension[0]
columna=dimension[1]
lista=[[fila for columna in range(columna)] for fila in range(numfila)]
print(lista)