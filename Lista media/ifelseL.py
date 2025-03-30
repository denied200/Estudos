#Ler o nome e o sexo de uma pessoa e apresentar como saída uma das seguintes mensagem:
#“Ilmo. Sr.”, caso seja informado o sexo como masculino, ou “Ilma. Sra.”, caso seja informado o
#sexo como feminino. Apresentar também junto com cada mensagem de saudação o nome
#previamente informado.

nome = (input("Insira o seu nome"))
sexo = int(input("Sexo masculino digite 1. Para sexo feminino digite 2"))

if sexo == 1:
    print ("Olá, Ilmo. Sr.",nome)
elif sexo == 2:
    print ('Olá, Ilma. Sra', nome)
else:
    print('Valor inválido')