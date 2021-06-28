# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:06:24 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre 
em graus Fahrenheit.

C = 5 * ((F-32) / 9).
"""

try:
    print("Programa que converte temperatura de graus Fahrenheit para Celsius\n")
    C = float(input("Digite a temperatura em graus Celsius: ")) 
    F = C*9/5 +32  
    print("\nTemperatura em graus Fahrenheit: R$ "+str(F)+"°F")
except ValueError:
        print("Erro! Digite apenas números!!")