# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:36:09 2021

@author: charlelito
charlelito@yahoo.com.br

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula:
    
    P = (72.7*altura) - 58
"""

print("Programa que calcula seu peso ideal com base na altura\n")

try:
    
    altura = float(input("Entre com sua altura em metros: "))
    peso = (72.7*altura) - 58
    
    print("\nSeu peso ideal é de: "+str(peso)+" kg")
     
except ValueError:
        print("Erro! Digite apenas números inteiros!!")