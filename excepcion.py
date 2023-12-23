try:
    n=float(input("introduce un numero: "))
    m=4
    print("{}/{} = {}".format(n,m,n/m))
    # o tambien puede ser
    print(n, "/", m, " = ",n/m)
except:
    print("ha ocurrido un error, introduce bien el numero")
else:
    print("todo ha funcionado correctamente")
finally:
    print("fin del programa")
    