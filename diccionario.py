ciudades={'santander': 'Bucaramanga', 'boyaca': 'tunja', 'casanare': 'yopal'}
print(ciudades)
print(ciudades['boyaca'])
print(len(ciudades))
print(ciudades.keys())
print(ciudades.values())
#quiero tener el valor de la clave:
print(ciudades.get('casanare'))
#eliminar la clave
del ciudades['santander']
print(ciudades)
#remplazar valor
ciudades['casanare']='aguazul'
print(ciudades)


