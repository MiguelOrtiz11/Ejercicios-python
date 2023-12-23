#hacer un programa que muestre un meno con la opcion de sumar dos numeros, con la opcion imprimir 
#el cuadrilatero de n filas y n columnas y por ultimo con la opcion de salir
bandera=0
while bandera==0:
    print("mi menu")
    print("1) calcular la suma de dos numeros")
    print("2) imprimir un cuadrilatero con n filas y n columnas")
    print("3) salir del programa")
    opcion=int(input("seleccione una opcion entre 1 y 3: "))
    if opcion==1:
        numero1=int(input("ingrese numero 1: "))
        numero2=int(input("ingrese numero 2: "))
        suma=numero1+numero2
        print("la suma de los dos numeros es: ", suma)
    elif opcion==2:
        filas=int(input("ingrese el numero de filas: "))
        columnas=int(input("ingrese el numero de columnas: "))
        for i in range(filas):
            for m in range(columnas):
                print("*",end="")
            print("")
    elif opcion==1:
        bandera=1
    else:
        print("opcion incorrecta, seleccione un numero entre 1 y 3")
print("fin programa")    