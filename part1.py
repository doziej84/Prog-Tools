# -*- coding: utf-8 -*-
"""
create sum with for loop
"""

# define variables
x=0
n=10
for i in range(n):
    x += x + 5*i
    #print(i, 'of' , n, 'variable-x', x)
    
print('final value of x after %i iterations= ' %(n), x)
print ('final value of x after %i iterations =%5.2f' %(n, x))

