# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:23:14 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
"""

print("Programa do link de internet\n")

try:
     
    fileSize = float(input("Tamanho do arquivo em MB: "))
    velLink = float(input("Velocidade do Link de Internet em Mbps: "))
    
    # fileSize em bits
    fileSize = fileSize * 8 * 1024**2
    # downtime em bps
    velLink = velLink * 1024**2
    # Tempo em s
    downTime = fileSize/velLink
    # Tempo em min
    downTime = downTime / 60
    
    print("\nTempo aproximado de download do arquivo : "+str(downTime)+" Minutos")

except ValueError:
        print("Erro! Digite apenas números inteiros!!")