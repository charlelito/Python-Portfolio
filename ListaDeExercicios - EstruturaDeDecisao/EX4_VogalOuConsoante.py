# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:50:38 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

# isto é um conjunto
vogais = {'a','e','i','o','u'}


print("Programa que verifica se uma letra digitada é vogal ou consoante\n")

  
letra =  str(input("Digite uma letra: "))

# pertinencia de conjuntos com operador in   
if letra.lower() in vogais:
    print("Vogal")
else:
    print("Consoante")