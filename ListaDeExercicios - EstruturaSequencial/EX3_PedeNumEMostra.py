# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:04:00 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""

try:
    print("Programa que pede um número e então mostre a mensagem O número informado foi [número].\n")
    num1 = float(input("Digite um número: "))
    print("O número informado foi "+str(num1))
except ValueError:
        print("Erro! Digite apenas números!!")

