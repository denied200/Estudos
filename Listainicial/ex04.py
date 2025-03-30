#Peça para que o usuário digite 3 valores, a, b e c. Em seguida, calcule o delta
#da fórmula de Báskara, onde delta = b² - 4.a.c. Com esse valor, calcule os
#valores de y1 e y2 e exiba-os na tela, sendo que:
#_______
#y1 = (-b + √ delta ) / (2.a)
#_______
#y2 = (-b - √ delta ) / (2.a) 
#* Para utilizar raiz quadrada, fazemos assim:
#from math import sqrt
#a = sqrt(b)

import math

a = float(input("Insira o valor de a"))
b = float(input("Insira o valor de b"))
c = float(input("Insira o valor de c"))

de = (b*b) - (4*a*c)
delta = math.sqrt(de)

y1 = (-b - delta) / (2*a)
y2 = (-b + delta) / (2*a)

print ("Os valores de y1 e y2 são consecutivamente:" , y1, y2 )
