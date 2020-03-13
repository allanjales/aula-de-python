#Define valores dados
dKm 	= 10
tS 	= 43*60+30

#Converte para milha e hora
dMi 	= dKm/1.61
tH	= tS/60/60

#Calcula paradas
velMiH	= dMi/tH
tmedMi	= 1/velMiH

#Exibe as paradas
print('Tempo médio por milha =', round(tmedMi*60,2),'min/Mi')
print('Velocidade média =', round(velMiH,2), 'Mi/h')
