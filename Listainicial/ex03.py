#Calcule o valor de a na equação a = √ b² + c². Em seguida, exiba na tela o valor de a.

print ("Calcule o valor de a na equação a = √ b² + c²")
b = float(input("Insira o valor de b"))
c = float(input("Insira o valor de c"))

import math
pre = (b * b) + (c * c)
a = math.sqrt(pre)

print("O valor de a na equação é:", a)

