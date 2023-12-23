#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
# al usuario por la contraseña hasta que introduzca la contraseña correcta.
contra='123'
intento=input("digite la contraseña: ")
while intento !=contra:
    print("la contraseña npes correcta")
    intento=input("digita la contraseña nuevamente: ")

print("contraseña correcta")
print("_________________________")
print("bienvenido al sistema")