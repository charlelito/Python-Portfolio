# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:06:14 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""

print("Programa de Folha de pagamento\n")

try:
    aliqIRPF = 0.11
    aliqINSS = 0.08
    aliqSind = 0.05
    
    salh = float(input("Qual é o seu salário por hora em Reais?: R$ "))
    horm = float(input("Qual é o número de horas que você trabalhou este mês: ")) 
    
    salBruto = salh*horm
    contIRPF = aliqIRPF*salBruto
    contINSS = aliqINSS*salBruto
    contSind = aliqSind*salBruto
    salLiqui = salBruto - (contIRPF+contINSS+contSind)
    
    print("\n+ Salário Bruto   : R$ "+str(salBruto))
    print("     - IR (11%)   : R$ "+str(contIRPF))
    print("    - INSS (8%)   : R$ "+str(contINSS)) 
    print("- Sindicato ( 5%) : R$ "+str(aliqSind)) 
    print("= Salário Liquido : R$ "+str(salLiqui)) 
    
except ValueError:
        print("Erro! Digite apenas números inteiros!!")