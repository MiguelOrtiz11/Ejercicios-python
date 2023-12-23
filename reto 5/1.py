#menu "registrar partido, ver resultados, tabla de clasificacion, salir"
#funciones "fecha, goles unab, goles equipo rival, nombre del equipo rival, nombre de la unab"
#mejor desarrolar con listas (burbuja)

from datetime import datetime
from datetime import timedelta

#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")

now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))

    




# opciones 

def menu():
    print("------------------------------")
    print("Seleccione una opción...")
    print("\t1 - registrar partido")
    print("\t2 - ver resultados")
    print("\t3 - tabla de clasificacion")
    print("\n\t0 - salir")




 #= []
aux = True
while aux:
    menu()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1
   