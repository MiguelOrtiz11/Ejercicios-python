#hacer un programa para una fruteria que ofrece manzanas a 4200 el kilo con descuento asi: 0 a 2
#kilos no tiene descuento hasta 5 kilos 10% de descuento
#hasta 10 kilos 15% de descuento y si es mayor a 10 kilos 20% de descuento
kilos=float(input("digite la cantidad de kilos a comprar "))
valorcompra=kilos*4200
if kilos<=2:
    descuento=0
    valorpagar=valorcompra-descuento
elif kilos<=5:
    descuento=valorcompra-0.10
    valorpagar=valorcompra-descuento
elif kilos<=10:
    descuento=valorcompra-0.15
    valorpagar=valorcompra-descuento
else:
    descuento=valorcompra*0.20
    valorpagar=valorcompra-descuento
print("la compra de: ", kilos, "kilos tiene un valor de: ", valorcompra, 
"\n pero usted tiene un descuento de por valor de: ", descuento, 
"\n) por lo tanto el valor a pagar es: ", valorpagar)