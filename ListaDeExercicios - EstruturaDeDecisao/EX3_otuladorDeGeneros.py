# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:02:58 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
"""

# Exercicio homofóbico

print("Programa que rotula gêneros\n")

  
sex =  str(input("Digite uma letra (F ou M): "))

   
if sex=="M":
    print("Masculino")
elif sex=="F":
   print("Feminino")
else:
    print("Sexo Inválido")