#hacer un programa que lea el nombre, seco y la edad de una persona. determine si es mayor de edad y de que sexo es .
nombre=input("digite su nombre: ")
sexo=input("digite 1 para hombre o 2 para mujer: ")
edad=int(input("digite su edad: "))
if edad>=18:
    if sexo=='1':
        print(nombre, " es un hombre y es mayor de edad")
    else:
        print(nombre, " es una mujer y es mayor de edad")    
elif sexo=='1':
    print(nombre, " es un hombre y es menor de edad") 
else:
    print(nombre, " es una mujer y es menor de edad")           