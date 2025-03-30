#Escreva um programa em Python que leia um único valor contendo três dígitos, por
#exemplo, 697. O seu programa deverá exibir o valor da dezena do número
#informado. Se o usuário digitar o número 697, seu programa deverá imprimir no
#vídeo apenas o número 9. Você deverá utilizar apenas o conteúdo apresentado em
#aula na resolução do problema.

numero = int(input("Digite um número de três dígitos: "))

# Calcula o valor da dezena extraindo o segundo dígito
dezena = (numero // 10) % 10

# Exibe o resultado
print(dezena)