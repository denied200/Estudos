#Peça para que o usuário digite 5 valores. Em seguida, mostre a média aritmética
#desses 5 valores (soma de todos os números, dividido por 5).

valores = []
for i in range(5):
    valor = float(input(f"Digite o valor {i+1}:"))
    valores.append(valor)

#Calcule a media aritmetica
soma = sum(valores)
media = soma /5

print(f"A media aritmética dos 5 valores é: {media}")
