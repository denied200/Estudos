#g) Ler quatro valores numéricos inteiros e apresentar os valores que são divisíveis por 2 e 3.

numeros = []
for i in range(4):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Filtra os números divisíveis por 2 e 3
divisiveis = [num for num in numeros if num % 2 == 0 and num % 3 == 0]

if divisiveis:
    print("Números divisíveis por 2 e 3:", divisiveis)
else:
    print("Nenhum número inserido é divisível por 2 e 3.")