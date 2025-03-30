#Escreva um programa que calcule e imprima no vídeo: a área de um retângulo e o
#seu perímetro. Lembrando que a área é calculada multiplicando-se o valor da base
#pelo valor da altura. O perímetro é a soma de todos os lados. Exibir os valores no
#vídeo com apenas duas casas decimais.

base = float(input("Insira o valor da base do retangulo"))

altura = float(input("Insira o valor da altura do retangulo"))

area = base * altura

perimetro = (base * 2) + (altura * 2)


print (f"O valor da área do retangulo é , {area:.2f}, O valor do perímetro do retangulo é, {perimetro:.2f}")