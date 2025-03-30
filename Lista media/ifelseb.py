numero = float(input("Insira o primeiro positivo ou negativo valor"))

if numero <= 0:
    total = abs(numero)
    print(total)
else:
    print(numero)