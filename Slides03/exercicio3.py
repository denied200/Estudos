#Escreva um programa em Python que calcule a quantidade de litros de combustível
#gasta em uma viagem, utilizando um automóvel que faz 10,5 km/l (quilômetros por
#litro). Para realizar o cálculo, o usuário deve fornecer o tempo gasto e a velocidade
#média. Seu programa deverá imprimir a quantidade de litros com quatro casas
#decimais.




tempo = float(input("Forneça o tempo gasto em horas"))
velocidade = float(input("Forneça a velocidade média em km/h"))

automovel = 10.5

#calculo de distancia percorrida
distancia_percorrida = tempo * velocidade

#calculo de combustivel
valor = distancia_percorrida / automovel

#valor formatado para 4 casas decimais
valor_formato = format(valor, ".4f")

print("A quantidade de gasolina gasta é de", valor_formato)
