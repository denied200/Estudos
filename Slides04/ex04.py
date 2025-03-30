#Escreva um programa em Python que leia três valores inteiros. Imprima-os em
#ordem crescente.

valor1 = int(input("Insira o primeiro valor inteiro"))
valor2 = int(input("Insira o segundo valor inteiro"))
valor3 = int(input("Insira o terceiro valor inteiro"))

valores = sorted([valor1,valor2,valor3])

print(valores)