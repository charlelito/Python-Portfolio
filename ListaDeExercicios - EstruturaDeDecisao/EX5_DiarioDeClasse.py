# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:59:19 2021

@author:  charlelito
charlelito@yahoo.com.br

Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

try:
    print("Programa Diario de Classe ")
    num1 = float(input("Entre com a primeira nota parcial do aluno: "))
    num2 = float(input("Entre com a segunda nota parcial do aluno: "))
    soma = num1+num2
    media =soma/2
    print("\nMédia : "+str(media))
    if media==10:
        print("Aprovado com Distinção")
    elif media<10 and media>=7:
        print("Aprovado")
    elif  media<7: 
        print("Reprovado")
    else:
        print("Valores inválidos!")           
except ValueError:
        print("Erro! Digite apenas números!!")