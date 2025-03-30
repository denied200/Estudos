#Escreva um programa em Python que leia um único valor contendo três dígitos, por
#exemplo, 697. O seu programa deverá inverter a ordem dos dígitos e imprimir o
#resultado no vídeo. Por exemplo, se o usuário digitar 697, o seu programa deverá
#imprimir no vídeo o valor 796. Você deverá utilizar apenas o conteúdo apresentado
#em aula na resolução do problema.

numero = int(input("Digite um número de três dígitos: "))

# Extrai cada dígito da unidade, dezena e centena
unidade = numero % 10
dezena = (numero // 10) % 10
centena = numero // 100

# Inverte a ordem dos dígitos
numero_invertido = (unidade * 100) + (dezena * 10) + centena

# Exibe o resultado
print(numero_invertido)