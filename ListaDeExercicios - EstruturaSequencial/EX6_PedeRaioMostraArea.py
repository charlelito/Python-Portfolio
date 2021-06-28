# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:38:02 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
# Import math Library
import math

try:
    print("Programa que pede o raio de um círculo, calcula e mostra sua área.\n")
    raio = float(input("Digite ao raio do círculo em metros: "))
    
    area = math.pi*raio**2
    
    print("\nA área calculada é: "+str(area)+" M^2")
except ValueError:
        print("Erro! Digite apenas números!!")