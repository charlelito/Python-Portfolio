# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:27:24 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que converta metros para centímetros.
"""
try:
    print("Programa que converte metros para centímetros\n")
    mts = float(input("Digite a medida em metros: "))
    cts = mts*100
    print("\nA medida em centimetros é: "+str(cts))
except ValueError:
        print("Erro! Digite apenas números!!")
