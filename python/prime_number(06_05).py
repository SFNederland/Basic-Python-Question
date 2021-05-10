# -*- coding: utf-8 -*-
"""prime_number(06.05)
Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :
"""

def asal(x):
  sayac = 0
  for i in range(1,x+1):
    if x%i == 0:
      sayac+=1
  if sayac<3 and x != 1:
    return True
  else:
    return False

n = list(range(1,(int(input("sayı giriniz :"))+1)))
asal_sayı = filter(asal,n)
print(list(asal_sayı))
