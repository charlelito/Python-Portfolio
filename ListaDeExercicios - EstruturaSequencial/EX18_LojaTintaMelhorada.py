# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:47:20 2021

@author: charlelito
charlelito@yahoo.com.br

Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00. 

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

"""

import math

print("Programa da Loja de Tintas melhorada\n")

try:
     
    cobertura = 1/3 # 1L por 3M2
    volumeLata18 = 18 # Litros
    precoLata18 = 80 # R$
    
    volumeLata3_6 = 3.6 # Litros
    precoLata3_6 = 25 # R$
    
    area = float(input("Tamanho da área a ser pintada em M^2: "))
    
    volumeTinta = area / cobertura
    
    numeroLatas18 = volumeTinta / volumeLata18    
    numeroLatasI18 = math.ceil(numeroLatas18);
    precoTotal18 = numeroLatasI18 * precoLata18
    
    numeroLatas3_6 = volumeTinta / volumeLata3_6    
    numeroLatasI3_6 = math.ceil(numeroLatas3_6);
    precoTotal3_6 = numeroLatasI3_6 * precoLata3_6
    
    if numeroLatas18 >= 1:
        x1 = numeroLatas18-(numeroLatas18 % 1)
        resto = volumeTinta - x1*volumeLata18
        x2 = resto / volumeLata3_6
        x2 = math.ceil(x2)      
       
    else:
        x1 = numeroLatas18-(numeroLatas18 % 1)
        resto18= volumeTinta - x1*volumeLata18
        
        x2 = numeroLatas3_6-(numeroLatas3_6 % 1)
        resto3_6= volumeTinta - x2*volumeLata3_6
        
        if (resto18 < resto3_6):  
            x1 = numeroLatasI18
            x2 = 0
        else:
            x1 = 0
            x2 = numeroLatasI3_6
    
    precomindisp = x1*precoLata18 + x2*precoLata3_6 
        
        
    print("\nVolume de tinta teórico necessário: "+str(volumeTinta)+" L")    
    
    print("\nNúmero de latas de 18L a serem compradas : "+str(numeroLatasI18))
    print("Volume de tinta comprado: "+str(numeroLatasI18*volumeLata18)+" L")  
    print("Preço total comprando latas de 18L : R$ "+str(round(precoTotal18,2)) )
    
    print("\nNúmero de latas de 3.6L a serem compradas : "+str(round(numeroLatasI3_6,0)) )
    print("Volume de tinta comprado: "+str(numeroLatasI3_6*volumeLata3_6)+" L") 
    print("Preço total comprando latas de 3.6L : R$ "+str(round(precoTotal3_6,2)) )
    
    print("\nOpção sem desperdício\n")
    print("Número de latas de 18L a serem compradas : "+str(x1) )
    print("Número de latas de 3.6L a serem compradas : "+str(round(x2,0)) )  
    print("Volume de tinta comprado: "+str(x1*volumeLata18 + x2*volumeLata3_6)+" L")  
    print("Preço total comprando latas de 18L : R$ "+str(round(precomindisp,2)) )

except ValueError:
        print("Erro! Digite apenas números inteiros!!")