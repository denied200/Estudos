#Antes do racionamento de energia ser decretado, quase ninguém falava em
#quilowatts, mas agora, todos incorporaram essa palavra em seu vocabulário.
#Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer
#um programa em Python que leia o valor do salário mínimo e a quantidade de
#quilowatts gasta por uma residência. O programa deverá calcular e imprimir no vídeo:
#o valor em reais de cada quilowatt;
# o valor em reais a ser pago pela residência;
# o novo valor a ser pago pela residência considerando um desconto de 10%.

salariomin = float(input("Insira o valor do salario minimo atualmente"))
quilowatts = float(input("Insira a quantidade usada de quilowatts"))

#Valor do kww = 100 quilowatts de energia
kww = salariomin * ( 1/7)

#Calculo de valor de  ada quilowatt
kw = kww / 100

#Valor em reais a ser pago pela residencia
valor = kw * quilowatts

#Novo valor a ser pago com 10% de desconto
valor10 = valor * 0.1

print ("O valor do quilowatt R$", kw)
print ("O valor a ser pago será de R$", valor)
print ("O valor a ser pago com desconto R$",valor10)


