from typing import Pattern


valores=['pan','leche','huevos','jamon','salchichas']
#metodos
#append - agrega un elemento al fnal de la lista
valores.append(2001)
print(valores)
#count - recibe un parametro y cuenta la cantidad de veces que aparece en la lista
(valores.count())
print(valores)
#extend - extiende una lista agregando un vlaor al final 
valores.extend([])
print(valores)
#index - devuelve el indice de su primera apaaricion en la lista
print(valores.index(100))
#insert - inserta el elemento x en la lista, en el indice i
valores.insert(2, 'carne')
print(valores)
#pop - devuelve el ultimo elemento de la lista y lo boraa
valores.pop()
print(valores)
#remove - recibe un argumento como elemento y borra su primera aparicion
valores.remove('jamon')
print(valores)
#reverse - invieerte el orden de los elementos de una lista
valores.reverse()
print(valores)
#sort - ordena los elementos de una lista
valores.sort()
print(valores)


