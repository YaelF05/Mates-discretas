"""
Created on Sun Mar 10 14:15:49 2024

@author: yaelf
"""

def MCD (num1, num2):
  if num1 == 0:
    return num2
  else:
    return MCD(num2 % num1, num1)


print(MCD(115, 15))
