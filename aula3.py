# nota1 = float(input("Adicione a nota do primeiro bimestre "))
# nota2 = float(input("Adicione a nota do segundo bimestre"))
# nota3 = float(input("Adicione a nota do terceiro bimestre"))
# nota4 = float(input("Adicione a nota do quarto bimestre"))

# soma = (nota1 + nota2 + nota3 + nota4)/4
# print(soma)

# print("Faça um programa transformando metros em centimetros")

# metros = float(input("calcule os centimetros dentro dos metros"))
# centimetros = metros*100
# print(centimetros)

# raio = float(input("Qual é a area total de um circulo"))
# area = 3.14159265359 * (raio**2)
# print(area)

# lado = float(input("Qual é ao lado"))
# print(lado*lado)

#valorhora = float(input("Quanto é seu salario"))
#horatrabalhada = float(input("Qual é as suas horas trabalhadas"))
#print(valorhora*horatrabalhada)


# fahre = float(input("Quantos fahre"))
# celcios = 5*((fahre-32)/9)
# print(celcios)

# celsius = float(input("Quantos fahre"))
# fahree = 32+(celsius*9/5)
# print(fahree)



#exer8
#numero1 = int(input("digite um numero inteiro"))
#numero2 = int(input("digite um numero inteiro"))
#numeroreal = float(input("digite um numero real"))
#print((numero1*2) * (numero2/2))
#print(numero1 * 3 + numeroreal)


#exer9

#altura = float(input("Qual sua altura?"))
#print(f"seu peso ideal é {(72.7*altura)-58}")

#exer10

#alturah = float(input("Qual sua altura?"))
#print(f"seu peso ideal é {(72.7*alturah)-58}")
#alturam = float(input("Qual sua altura?"))
#print(f"seu peso ideal é {(62.1*alturam)-44.7}")

#exer11

#peso = float(input("peso dos peixes"))
#excesso = peso - 50
#multa = excesso*4
#print(peso-50)
#print(multa)


#exer12

totalsalario = float(input("Quanto é seu salario"))
valorhora = float(input("Quantas horas você trabalha por mês"))
ir= totalsalario * 0.11
inss= totalsalario * 0.08
sindicato= totalsalario *0.05
salarioliquido= (((totalsalario - ir)-inss)-sindicato)  
print(f"Salário Bruto R$ {totalsalario:.2f}\nIRF R$ {ir}\nINSS R$ {inss}\nSINDICATO R$ {sindicato}\nSALARIO LIQUIDO R${salarioliquido}")
