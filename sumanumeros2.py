totalSuma = 0
primerNumero = int(input("Digite el primer numero: "))
segundoNumero = int(input("Digite el segundo numero: "))
sumaNumeros = primerNumero + segundoNumero
totalSuma = totalSuma + sumaNumeros
print("la suma es:", + sumaNumeros)
pedirNumero = input("Desea realizar otra suma? (s/n)")
while pedirNumero == "s": 
    primerNumero = int(input("Digite el primer numero: "))
    segundoNumero = int(input("Digite el segundo numero: "))
    sumaNumeros = primerNumero + segundoNumero
    totalSuma = totalSuma + sumaNumeros
    print("la suma es:", + sumaNumeros)
    pedirNumero = input("Desea realizar otra suma? (s/n)")
else:
    print("la suma total de todos los numeros digitadoes es: ", + totalSuma)
