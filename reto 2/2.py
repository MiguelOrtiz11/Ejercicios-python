#   Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o 
#   superiores a $2’000,000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
#   mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad=int(input("digite su edad: "))
ingresos=int(input("digite sus ingrsos mensuales: "))
if edad>=18:
    if ingresos>=2000000:
        print("tiene que tributar")
else:
    print("no tiene que tributar")