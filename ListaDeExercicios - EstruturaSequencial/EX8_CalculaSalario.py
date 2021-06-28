# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:51:07 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
try:
    print("Programa seu calcula salário mensal\n")
    salh = float(input("Qual é o seu salário por hora em Reais?: R$ "))
    horm = float(input("Qual é o número de horas que você trabalhou este mês: ")) 
    salm = salh*horm
    print("\nSeu salário neste mês será: R$ "+str(salm))
except ValueError:
        print("Erro! Digite apenas números!!")