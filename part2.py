# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:12:18 2022

@author: Admin
"""

# pi= 0
# n=10

# for k in range(n):
#     k += k + 8*(1./(((4*k) +1)*((4*k)+1)))
    
# print('final value of pi after %i iterations= ' %(n), k)
    


import numpy 
#n =10
def my_pi(n):
    pi=0
    for k in range(n):
        pi += 1./(((4*k) +1)*((4*k)+3))
    pi *=8
    return pi

for n in [10, 50, 100, 1000]:
    pi = my_pi (n)
print( 'pi approx =', pi)
print ('error =', abs(pi-numpy.pi), 'after %i iterations'% (n) )

print (my_pi(1000))
      

    