# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:58:24 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

print("Programa que descobre se um número é positivo ou negativo\n")

try:     
    n1 = float(input("Digite um número: "))

    if n1 >=0:
        print("O número "+str(n1)+" é positivo!")
    else:
        print("O número "+str(n1)+" é negativo!")

except ValueError:
        print("Erro! Digite apenas números!")