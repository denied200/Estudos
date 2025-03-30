valor1 = int(input("Insira a pontuacao do primeiro lugar"))
valor2 = int(input("Insira a pontuacao do segundo lugar"))
valor3 = int(input("Insira a pontuacao do terceiro lugar"))

#O vice campeao e sempre o do meio
 
valor = sorted([valor1, valor2, valor3])[1]

print("O vice campeao tem a pontuacao de:", valor)