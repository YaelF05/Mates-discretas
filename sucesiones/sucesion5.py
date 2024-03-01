# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 18:58:56 2024

@author: yaelf
"""
numero = int(input("Ingresa un número: "))

for i in range (1, numero + 1):
    numerador = i**2
    denominador =  3**i
    
    print(i**2,"/",3**i)