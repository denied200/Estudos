valores = []
for i in range(4):
    valor = float(input(f"Digite o valor {i+1}:"))
    valores.append(valor)

#Calcule a media aritmetica
soma = sum(valores)
total = soma /4

if total >= 5:
    print("Aprovado!")
else:
    print("Reprovado :(")