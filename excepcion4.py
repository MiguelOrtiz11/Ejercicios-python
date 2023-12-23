import sys
try:
    4+saludo*3
except NameError:
    print("nombre de variablo no existe")
    print("el error fue: ", sys.exc_info())[0]
