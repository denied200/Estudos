numero1 = int(input("Insira o primeiro valor"))
numero2 = int(input("Insira o segundo valor"))

if numero1 > numero2:
    dif = numero1 - numero2
    print ('A diferença entre o menor e o maior número é de', dif)
elif numero1 < numero2:
    dif = numero2 - numero1
    print ('A diferença entre o menor e o maior número é de', dif)