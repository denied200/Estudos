#Ler um valor numérico inteiro que esteja na faixa de valores de 1 até 9. O programa deve
#apresentar a mensagem “O valor está na faixa permitida”, caso o valor informado esteja entre
#1 e 9. Se o valor estiver fora da faixa, o programa deve apresentar a mensagem “O valor está
#fora da faixa permitida”.

valor1 = int(input("Insira o valor inteiro entre 1-9 ou maior"))

if valor1 <= 9 and valor1 >= 1:
    print ("O valor esta na faixa permitida")
else:
    print ("O valor esta fora da faixa permitida")
