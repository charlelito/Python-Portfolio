# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:36:09 2021

@author: charlelito
charlelito@yahoo.com.br

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

print("Programa que calcula seu peso ideal com base na altura\n")

try:
    
    altura = float(input("Entre com sua altura em metros: "))
    pesoH = (72.7*altura) - 58
    pesoM = (62.1*altura) - 58
    
    print("\nGênero masculino, seu peso ideal é de: "+str(pesoH)+" kg")
    print("\nGênero feminino, seu peso ideal é de: "+str(pesoM)+" kg")
 
except ValueError:
        print("Erro! Digite apenas números inteiros!!")