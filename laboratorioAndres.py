import random

matrizAlfabeto = [None] * 6
for i in range(0,6):
    matrizAlfabeto[i] = [None] * 10

for i in range(0,6):
    for j in range(0,10):
        matrizAlfabeto[i][j] = round((random.uniform(0,10)), 1)
#print(matrizAlfabeto)

julioCali = matrizAlfabeto[0][0]
julioBogota = matrizAlfabeto[0][1]
julioMedellin = matrizAlfabeto[0][2]
julioBarranquilla = matrizAlfabeto[0][3]
julioManizales = matrizAlfabeto[0][4]
julioPereira = matrizAlfabeto[0][5]
julioPasto = matrizAlfabeto[0][6]
julioSantamarta = matrizAlfabeto[0][7]
julioCucuta = matrizAlfabeto[0][8]
julioCartagena = matrizAlfabeto[0][9]

agostoCali = matrizAlfabeto[1][0]
agostoBogota = matrizAlfabeto[1][1]
agostoMedellin = matrizAlfabeto[1][2]
agostoBarranquilla = matrizAlfabeto[1][3]
agostoManizales = matrizAlfabeto[1][4]
agostoPereira = matrizAlfabeto[1][5]
agostoPasto = matrizAlfabeto[1][6]
agostoSantamarta = matrizAlfabeto[1][7]
agostoCucuta = matrizAlfabeto[1][8]
agostoCartagena = matrizAlfabeto[1][9]

septiembreCali = matrizAlfabeto[2][0]
septiembreBogota = matrizAlfabeto[2][1]
septiembreMedellin = matrizAlfabeto[2][2]
septiembreBarranquilla = matrizAlfabeto[2][3]
septiembreManizales = matrizAlfabeto[2][4]
septiembrePereira = matrizAlfabeto[2][5] 
septiembrePasto = matrizAlfabeto[2][6] 
septiembreSantamarta = matrizAlfabeto[2][7]
septiembreCucuta = matrizAlfabeto[2][8]
septiembreCartagena = matrizAlfabeto[2][9]

octubreCali = matrizAlfabeto[3][0]
octubreBogota = matrizAlfabeto[3][1]
octubreMedellin = matrizAlfabeto[3][2]
octubreBarranquilla = matrizAlfabeto[3][3]
octubreManizales = matrizAlfabeto[3][4]
octubrePereira = matrizAlfabeto[3][5] 
octubrePasto = matrizAlfabeto[3][6] 
octubreSantamarta = matrizAlfabeto[3][7]
octubreCucuta = matrizAlfabeto[3][8]
octubreCartagena = matrizAlfabeto[3][9]

noviembreCali = matrizAlfabeto[4][0]
noviembreBogota = matrizAlfabeto[4][1]
noviembreMedellin = matrizAlfabeto[4][2]
noviembreBarranquilla = matrizAlfabeto[4][3]
noviembreManizales = matrizAlfabeto[4][4]
noviembrePereira = matrizAlfabeto[4][5] 
noviembrePasto = matrizAlfabeto[4][6] 
noviembreSantamarta = matrizAlfabeto[4][7]
noviembreCucuta = matrizAlfabeto[4][8]
noviembreCartagena = matrizAlfabeto[4][9]

diciembreCali = matrizAlfabeto[5][0]
diciembreBogota = matrizAlfabeto[5][1]
diciembreMedellin = matrizAlfabeto[5][2]
diciembreBarranquilla = matrizAlfabeto[5][3]
diciembreManizales = matrizAlfabeto[5][4]
diciembrePereira = matrizAlfabeto[5][5] 
diciembrePasto = matrizAlfabeto[5][6] 
diciembreSantamarta = matrizAlfabeto[5][7]
diciembreCucuta = matrizAlfabeto[5][8]
diciembreCartagena = matrizAlfabeto[5][9]


def promedioMes():

    julio = ((julioCali + julioBogota + julioMedellin + julioBarranquilla + julioManizales + julioPereira + julioPasto + julioSantamarta + julioCucuta + julioCartagena) /10)
    agosto = ((agostoCali + agostoBogota + agostoMedellin + agostoBarranquilla + agostoManizales + agostoPereira + agostoPasto + agostoSantamarta + agostoCucuta + agostoCartagena) /10)
    septiembre = ((septiembreCali + septiembreBogota + septiembreBarranquilla + septiembreManizales + septiembrePereira + septiembrePasto + septiembreSantamarta + septiembreCucuta + septiembreCartagena) /10)
    octubre = ((octubreCali + octubreBogota + octubreBarranquilla + octubreManizales + octubrePereira + octubrePasto + octubreSantamarta + octubreCucuta + octubreCartagena) /10)
    noviembre = ((noviembreCali + noviembreBogota + noviembreBarranquilla + noviembreManizales + noviembrePereira + noviembrePasto + noviembreSantamarta + noviembreCucuta + noviembreCartagena) /10)   
    diciembre = ((diciembreCali + diciembreBogota + diciembreBarranquilla + diciembreManizales + diciembrePereira + diciembrePasto + diciembreSantamarta + diciembreCucuta + diciembreCartagena) /10)

    pedirMes = input("ingrese un mes desde julio hasta diciembre: ")

    if (pedirMes == "julio"):
        print("El promedio de inflaciones en julio es de: ", + julio)
    elif (pedirMes == "agosto"):
        print("El promedio de inflaciones en agosto es de: ", + agosto)
    elif (pedirMes == "septiembre"):
        print("El promedio de inflaciones en septiembre es de: ", + septiembre)
    elif (pedirMes == "octubre"):
        print("El promedio de inflaciones en octubre es de: ", + octubre)
    elif (pedirMes == "noviembre"):
        print("El promedio de inflaciones en noviembre es de: ", + noviembre)
    elif (pedirMes == "diciembre"):
        print("El promedio de inflaciones en diciembre es de: ", + diciembre)


def promedioCiudad():

    cali = (julioCali + agostoCali + septiembreCali + octubreCali + noviembreCali + diciembreCali)       
    bogota = (julioBogota + agostoBogota + septiembreBogota + octubreBogota + noviembreBogota + diciembreBogota)    
    medellin = (julioMedellin + agostoMedellin + septiembreMedellin + octubreMedellin + noviembreMedellin + diciembreMedellin)     
    barranquilla = (julioBarranquilla + agostoBarranquilla + septiembreBarranquilla + octubreBarranquilla + noviembreBarranquilla + diciembreBarranquilla)
    manizales = (julioManizales + agostoManizales + septiembreManizales + octubreManizales + noviembreManizales + diciembreManizales)
    pereira = (julioPereira + agostoPereira + septiembrePereira + octubrePereira + noviembrePereira + diciembrePereira)    
    pasto = (julioPasto + agostoPasto + septiembrePasto + octubrePasto + noviembrePasto + diciembrePasto)       
    santamarta = (julioSantamarta + agostoSantamarta + septiembreSantamarta + octubreSantamarta + noviembreSantamarta + diciembreSantamarta)       
    cucuta = (julioCucuta + agostoCucuta + septiembreCucuta + octubreCucuta + noviembreCucuta + diciembreCucuta)     
    cartagena = (julioCartagena + agostoCartagena + septiembreCartagena + octubreCartagena + noviembreCucuta + diciembreCucuta)
            
    pedirCiudad=input("ingrese una ciudad de Cali, Bogota, Medellin, Barranquilla, Manizales, Pereira, Pasto, SantaMarta, Cucuta o Cartagena: ")
    
    if (pedirCiudad == "cali"):
        print("El promedio de las inflaciones en la ciudad de Cali es: ", + cali)
    elif (pedirCiudad == "bogota"):
        print("El promedio de las inflaciones en la ciudad de Bogota es: ", + bogota)
    elif (pedirCiudad == "medellin"):
        print("El promedio de las inflaciones en la ciudad de Medellin es: ", + medellin)
    elif (pedirCiudad == "barranquilla"):
        print("El promedio de las inflaciones en la ciudad de Barranquilla es: ", + barranquilla)
    elif (pedirCiudad == "manizales"):
        print("El promedio de las inflaciones en la ciudad de Manizales es: ", + manizales)
    elif (pedirCiudad == "pereira"):
        print("El promedio de las inflaciones en la ciudad de Pereira es: ", + pereira)
    elif (pedirCiudad == "pasto"):
        print("El promedio de las inflaciones en la ciudad de Pasto es: ", + pasto)
    elif (pedirCiudad == "santa marta"):
        print("El promedio de las inflaciones en la ciudad de Santa Marta es: ", + santamarta)
    elif (pedirCiudad == "cucuta"):
        print("El promedio de las inflaciones en la ciudad de Cucuta es: ", + cucuta)
    elif (pedirCiudad == "cartagena"):
        print("El promedio de las inflaciones en la ciudad de Cartagena es: ", + cartagena)


print("__________________________________________________")

menu = input("Seleccione una opcion: \n1. Registrar las inflaciones en la matriz \n2. Desplegar la matriz de inflaciones \n3. Promedio de inflacion por mes \n4. Promedio de inflacion por ciudad \nIngresar el numero: ")

if (menu == "1"):
    print("se registraron las inflaciones con exito")

elif (menu == "2"):
    print(matrizAlfabeto)

elif (menu == "3"):
    promedioMes()

elif (menu == "4"):
    promedioCiudad()

pedirValor = input("Desea volver a registrar una opcion? s/n:   ")

while pedirValor == "s":
    
    menu = input("Seleccione una opcion: \n1. Registrar las inflaciones en la matriz \n2. Desplegar la matriz de inflaciones \n3. Promedio de inflacion por mes \n4. Promedio de inflacion por ciudad \nIngresar el numero: ")
    
    if (menu == "1"):
        print("se registraron las inflaciones con exito")

    elif (menu == "2"):
        print(matrizAlfabeto)

    elif (menu == "3"):
        promedioMes()

    elif (menu == "4"):
        promedioCiudad()
    
    pedirValor = input("Desea volver a registrar una opcion? s/n:   ")

else:
    print("Ah finalizado el programa con exito :D")

print("__________________________________________________")

