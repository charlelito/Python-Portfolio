# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:47:22 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

try:
    print("Programa que calcula a área de um quadrado e mostra o dobro desta área\n")
    lado = float(input("Digite a medida do lado do quadrado em metros: "))
    darea = 2*(lado**2)
    
    print("\nO dobro da área é: "+str(darea))
except ValueError:
        print("Erro! Digite apenas números!!")