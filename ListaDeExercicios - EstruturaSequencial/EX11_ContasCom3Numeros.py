# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:16:02 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
    1 - o produto do dobro do primeiro com metade do segundo .
    2 - a soma do triplo do primeiro com o terceiro.
    3 - o terceiro elevado ao cubo.
"""

print("Programa que faz contas aleatórias com 3 números\n")

try:
    
    num1 = int(input("Entre com o primeiro número inteiro: "))
    num2 = int(input("Entre com o segundo número inteiro: "))
     
except ValueError:
        print("Erro! Digite apenas números inteiros!!")

try:
    
    num3 = float(input("Entre com o terceiro número real: "))
     
except ValueError:
        print("Erro! Digite apenas números!!")
    
try:
    
    res1 = (2*num1)*(num2/2)
    res2 = (3*num1)+num3
    res3 = num3**3
    
    print("1 - O produto do dobro do primeiro com metade do segundo: "+str(res1))
    print("2 - A soma do triplo do primeiro com o terceiro: "+str(res2))
    print("3 - O terceiro elevado ao cubo: "+str(res3))
    
except ValueError:
        print("Erro!")