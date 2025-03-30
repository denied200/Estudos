#Construa um programa em Python que leia três valores inteiros. Caso os três valores
#informados sejam diferentes entre si, imprima no vídeo o menor valor. Se os valores
#não forem diferentes apresente uma mensagem informando o usuário.

while True:
    valor1 = int(input("Insira o primeiro valor inteiro"))
    valor2 = int(input("Insira o segundo valor inteiro"))
    valor3 = int(input("Insira o terceiro valor inteiro"))

    if valor1 != valor2 != valor3:
      valor = min(valor1,valor2,valor3)
      print("O menor valor e:", valor)