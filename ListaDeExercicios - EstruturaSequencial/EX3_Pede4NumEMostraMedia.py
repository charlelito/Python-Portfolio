# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:04:00 2021

@author: charlelito
charlelito @yahoo.com.br

Faça um Programa que peça as 4 notas bimestrais e mostre a média..
"""

try:
    print("Programa que pede as 4 notas bimestrais e mostre a média..\n")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4)/4
    print("\nA média foi "+str(media))
except ValueError:
        print("Erro! Digite apenas números!!")