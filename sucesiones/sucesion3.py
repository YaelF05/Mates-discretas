# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:37:49 2024

@author: yaelf
"""
     
numero  = int(input("Ingresa un número: "))

for i in range(1, numero + 1):
    numerador = i
    denominador = (1 + i )**2
    print(f"{numerador}/{denominador}" )