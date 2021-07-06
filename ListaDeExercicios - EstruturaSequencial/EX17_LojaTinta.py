# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 16:23:14 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

print("Programa da Loja de Tintas\n")

try:
     
    cobertura = 1/3 # 1L por 3M2
    volumeLata = 18 # Litros
    precoLata = 80 # R$
    
    area = float(input("Tamanho da área a ser pintada em M^2: "))
    
    volumeTinta = area / cobertura
    numeroLatas = volumeTinta / volumeLata
    numeroLatas = round(numeroLatas,0)
    precoTotal = numeroLatas * precoLata
    
    print("\nNúmero de latas a serem compradas : "+str(numeroLatas) )
    print("\nPreço total : R$ "+str(round(precoTotal,2)) )

except ValueError:
        print("Erro! Digite apenas números inteiros!!")