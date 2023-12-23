nom = input('Cual es tu nombre: ')
ciu = input('De cual de las ciudades eres: Cali, Tunja, Manizales: ')
num_adul = int(input('Cuantos adultos son: '))
num_ni = int(input ('Cuanto ninos son: '))    
num_est = int(input('Cuanto tiempo estaras: '))
tipoPlan = input('Digite el numero correspondiente\n 1- plan con tiquete aereo \n 2- Solo hotel \n 3- plan terrestre: ')

def tiqueteAereo():
    cali = 0
    tunja = 0
    manizales = 0
    costoTiquete = 0
    ciu = cali, tunja, manizales
    

    if ciu == cali:
        ciu = 850000
    elif ciu == tunja:
        ciu = 630000
    elif ciu == manizales:
        ciu = 480000

    num_adulto = num_adul * 230000
    num_nino = num_ni * 120000

    costoTiquete = num_adulto + num_nino + ciu
    print(costoTiquete)

print('---------------------------------------')
print('Solicitante: ' + nom)
print('Ciudad de origen: ' + ciu)
print('Numero de adultos: ' + str(num_adul))
print('Numero de niños: ' + str(num_ni))
print('Numero de dias: ' + str(num_est))
print('Tipo de plan: ' + tipoPlan)
print('Costo cotizacion: ' + tiqueteAereo())
    


    

    
        
    
    