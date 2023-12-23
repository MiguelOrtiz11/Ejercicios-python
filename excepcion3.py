num1=int(input("ingrese el numero divisor: "))
num2=int(input("ingrese el numero dividendo: "))
try:
    resultado=num1/num2
except ZeroDivisionError:
    print("no se puede dividir entre cero!!!")
else:
    print(resultado)
finally: 
    print("fin del programa")
    