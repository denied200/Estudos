#Elaborar um programa em Python para calcular o valor do salário líquido mensal de
#um professor do ensino fundamental. Para o cálculo do salário mensal do professor
#são necessários os seguintes dados: valor da hora-aula, número de horas
#trabalhadas no mês e a porcentagem de desconto do INSS. O cálculo do salário leva
#em consideração os seguintes passos:

#a) calcula-se o valor do salário bruto (valor da hora-aula multiplicada pelo número
#de horas trabalhadas).

#b) A partir do salário bruto, calcula-se o valor que será descontado referente ao
#INSS.

#c) Calcula-se o salário líquido mensal (valor do salário bruto menos o valor do
#desconto do INSS.

#d) Exibir o valor do salário líquido com apenas duas casas decimais.

hora_aula = float(input("Insira o valor da hora da aula dada"))
trabalhadas = float(input("Insira o numero de horas trabalhadas no mes "))
inss = float(input("Insira a porcentagem de desconto do INSS apenas em valor"))

#exercicio A
bruto = hora_aula * trabalhadas

#exercicio B
desconto = bruto * inss

#exercicio C
liquido = bruto - inss

#exercicio D
print (f"O salario liquido é R$ {liquido:.2f}")



