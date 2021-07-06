# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:46:59 2021

@author: charlelito
charlelito@yahoo.com.br

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
que você faça um programa que leia a variável peso (peso de peixes) e calcule 
o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
na variável multa o valor da multa que João deverá pagar. Imprima os dados do 
programa com as mensagens adequadas.
"""

print("Programa do João Papo-de-Pescador\n")

try:
    
    limitePeso = 50.0
    multaPesoExcedente = 4.0
    
    peso = float(input("Entre com o peso dos peixes: "))
    excesso = peso - limitePeso
    if excesso < 0:
       excesso = 0
    
    multa = excesso*multaPesoExcedente
    
    print("\nExcesso de peso de: "+str(excesso)+" kg")
    print("\nMulta devida de: R$ "+str(multa))
 
except ValueError:
        print("Erro! Digite apenas números!!")

