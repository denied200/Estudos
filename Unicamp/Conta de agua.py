#Até 10 metros: incluído na franquia;
#11 a 30 metros: R$ 1 por metro excedente;
#31 a 100 metros: R$ 2 por metro excedente;
#101 metros em diante: R$ 5 por metro excedente.
while True:
    consumo = int(input("Insira o seu consumo de agua em m3"))

#taxa fixa
    fixo = 7


    if consumo <= 10:
        print (f"Voce tera que pagar R${fixo}")
    elif consumo in range (11,30):
        print(f"Voce tera que pagar R${((consumo - 10)* 1)+ 7}")
    elif consumo in range (31,100):
        print(f"Voce tera que pagar R${((consumo - 30)*2) + 7 + 20}")
    elif consumo in range (100,121):
        print (f"Voce tera que pagar R${((consumo - 100)*5)+7 +20 + 140}")
    