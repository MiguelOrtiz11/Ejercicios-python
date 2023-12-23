from math import factorial
#funciones
def factorialrecursivo(n):
    return 1 if n==0 else n*factorialrecursivo(n-1)

def facto(n):
    facto_resp=1
    while n>1:
        facto_resp=facto_resp*n
        n=n-1
    return facto_resp

#cuerpo del programa
a=factorialrecursivo(3)
print("el factorial de forma recursiva de 5 es: ", a)

b=facto(5)
print("el factorial de forma iterativa de 5 es: ", b)

c=factorial(5)
print("el factorial de la funcion de python de 5 es: ", b)