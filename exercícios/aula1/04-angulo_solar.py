import math

#Definição de variáveis
altura = 5
sombra = 0.5

#Calculos
anguloRad = math.atan(sombra/altura)
anguloGrau = anguloRad*180/math.pi

#Exibição dos resultados
print('O ângulo de zênite do Sol é de ', round(anguloGrau, 2), '°', sep='')
