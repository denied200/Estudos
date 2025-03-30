#Escreva um programa que leia uma temperatura em graus Celsius e apresente no
#vídeo a sua equivalente em graus Fahrenheit. A fórmula de conversão é:
#𝐹 = 𝐶 ∗ (9 / 5) + 32
#onde C é a temperatura em graus Celsius e F a temperatura em graus Fahrenheit.
#Exiba a temperatura no vídeo com três casas decimais.

c = float(input("Insira a temperatura em celcius que será covertida para fahrenheit"))

f = (c * (9 / 5)) + 32

print(f"A temperatura convertida é de {f:.3f} graus fahrenheit")