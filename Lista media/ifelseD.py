def calcular_media():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    
# Calcular a média aritmética
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
    
# Verificar aprovação ou necessidade de exame
    if media >= 7:
        print(f"Aprovado com média {media:.2f}")
    else:
        exame = float(input("Digite a nota do exame: "))
        nova_media = (media + exame) / 2
        print(f"Nova média: {nova_media:.2f}")
        
    if nova_media >= 5:
        print(f"Aprovado em exame com média {nova_media:.2f}")
    else:
        print(f"Reprovado com média {nova_media:.2f}")

# Executar o programa
calcular_media()
