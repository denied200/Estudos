primeiro = float(input("Insira o primeiro número"))
print (primeiro)
op = (input("Insira a sua operação, +, /, - ou *"))
print(primeiro,op)
segundo = float(input("Insira o segundo número"))
print (primeiro,op,segundo)

if op == "+":
    print (primeiro + segundo)
elif op == "-":
    print (primeiro - segundo)
elif op == "*":
    print (primeiro * segundo)
elif op == "/":
    print (primeiro / segundo)
else:
    print ("Não foi possível realizar a sua conta")