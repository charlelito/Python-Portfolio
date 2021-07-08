# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:47:54 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça dois números e imprima o maior deles.
"""

print("Programa que descobre o maior de dois números\n")

try:     
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if n1 > n2:
        print("O maior número é "+str(n1))
    elif n2 > n1:
        print("O maior número é "+str(n2))
    else:
        print("Os dois números são iguais!")

except ValueError:
        print("Erro! Digite apenas números!")