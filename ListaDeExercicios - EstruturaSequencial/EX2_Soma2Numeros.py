# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:18:55 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça dois números e imprima a soma
"""

try:
    print("Programa que soma números\n")
    num1 = float(input("Entre com o primeiro número: "))
    num2 = float(input("Entre com o segundo número: "))
    soma = num1+num2
    print(str(num1)+"+"+str(num2)+"="+str(soma))
except ValueError:
        print("Erro! Digite apenas números!!")

