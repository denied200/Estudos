#Ler um valor numérico inteiro e apresentar uma mensagem informando se o valor é par ou
#ímpar.

valor1 = int(input("Insira o valor inteiro para verificar se o valor e par ou impar"))

if valor1 % 2 == 0:
    print(" O valor e par")
else:
    print ("O valor e impar")