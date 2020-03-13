import math

#Definição de variáveis
massa 	= 11
altura 	= 0.70

#Calculos
imc = massa/pow(altura,2)

#Exibição dos resultados
print('O IMC do bebê é', round(imc, 2))

#Verificação
if imc >= 20 and imc <= 25:
	print('Portanto o bebê é saudável')
else:
	print('O bebê não está saudável :(')
