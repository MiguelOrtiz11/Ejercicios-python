#funciones
def fibonacci(numero):
    return 0 if numero==0 else 1 if numero==1  else fibonacci(numero-1)+fibonacci(numero-2)

#de forma iterativa
def fibo(num):
    if num<2:
        return num 
    else:
        return fibo(num-1)+fibo(num-2)


print(" 0 1 1 2 3 5 8 13 21 34 55 89 144 233 ")
#cuerpo del programa
a=fibonacci(11)
print("el resultado de la serie fibonacci de forma recursiva es: ", a)
b=fibo(5)
print("el resultado de la serie fibonacci de forma iterativa es: ", b)


numeros=int(input("digite un numero a calcular fibonacci: "))
for i in range(numeros+1):
    print(fibo(i))
