#Ler cinco valores numéricos inteiros, identificar e apresentar o maior e o menor valor
#informado. Não execute a ordenação dos valores.

valor1 = int(input("Insira o primeiro valor inteiro"))
valor2 = int(input("Insira o segundo valor inteiro"))
valor3 = int(input("Insira o terceiro valor inteiro"))
valor4 = int(input("Insira o segundo valor inteiro"))
valor5 = int(input("Insira o terceiro valor inteiro"))

maior = max(valor1,valor2,valor3,valor4,valor5)
menor = min(valor1,valor2,valor3,valor4,valor5)

print("Números:", maior , menor)
