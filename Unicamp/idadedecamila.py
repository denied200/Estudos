valor1 = int(input("Insira a primeira idade"))
valor2 = int(input("Insira a segunda idade"))
valor3 = int(input("Insira a terceira idade"))

#A idade de Camila sempre sera a do meio
 
valor = sorted([valor1, valor2, valor3])[1]

print("a idade de camila e:", valor)