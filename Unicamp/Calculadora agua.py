# Deseja-se criar um programa de computador para calcular o valor da conta de água de
# uma residência. Sabe-se que o valor de 1.000 litros de água corresponde a 2% do valor do
# salário mínimo” 

salariomin = int(input("insira o salario minimo"))
litro = int(input("insira os litros de agua usados"))
porcento = salariomin * 0.02
agua = porcento / 1000

#porcento é o valor para 1000 litros de água

total = litro * agua


if total > 1:
   print("O valor da sua conta de água é", (total) ,"reais")
elif total == 0:
   print ("Você não pagará nada!!!")
else: 
    print ("O valor da sua conta de água é", (total) ,"real")