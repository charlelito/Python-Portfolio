# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:06:24 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).
"""

try:
    print("Programa que converte temperatura de graus Fahrenheit para Celsius\n")
    F = float(input("Digite a temperatura em graus Fahrenheit: ")) 
    C = 5*((F-32)/9)
    print("\nTemperatura em graus Celsius: R$ "+str(C)+"°C")
except ValueError:
        print("Erro! Digite apenas números!!")