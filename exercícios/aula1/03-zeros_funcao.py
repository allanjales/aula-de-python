import math

#Definição de variáveis
a = 3
b = -4
c = -10

#Calculos
delta 	= math.pow(b, 2) - 4*a*c
x1	= (-b + math.sqrt(delta))/(2*a)
x2	= (-b - math.sqrt(delta))/(2*a)

#Exibição dos resultados
print('As raízes da equação y = 3x² - 4x -10 são ', round(x1,2), 'e', round(x2,2))
