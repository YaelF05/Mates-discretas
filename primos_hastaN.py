# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:41:37 2024

@author: yaelf
"""

numero = int(input("Escribe un número: ")) 

for i in range (2, numero + 1):
    primo = True
    for j in range(2,i // 2 + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)