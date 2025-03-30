#Um hotel cobra R$ 250,00 a diária e mais uma taxa de serviços. A taxa de serviços é
#de:
#R$ 22,50 por diária, se o número de diárias for maior que 15;
#R$ 56,00 por diária, se o número de diárias for igual a 15;
#R$ 88,00 por diária, se o número de diárias for menor que 15.
#Construa um programa em Python que calcule e imprima o valor da conta de um
#cliente.


diaria = int(input("Insira a quantidade de dias que voce deseja ficar no hotel"))
taxa = 250

if diaria > 15:
    preco = 22,5

elif diaria == 15:
    preco = 56

elif diaria < 15:
    preco = 88

valor = preco + taxa

print("O preço da sua estadia em nosso hotel será R$:",valor)
