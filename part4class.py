# -*- coding: utf-8 -*-
"""
Check if list of divisors results in modulo =0 (python %)
"""

def get_divisor(int_in):
    div_all =[2,3,4,5,6,7,8,9]
    
    div_out=[]
    
    #check which divisors has modulo 0
    for curr_div in div_all:
        modulo = int_in%curr_div
        if modulo ==0 and curr_div !=int_in:
            # add this number to list
            div_out.append(curr_div)
        return div_out
            
            
## generate simple test case
my_int= 6 # return should be [2,3,4,6]
div_out = get_divisor(my_int)
print("int input:%i, divisors=%s"%(my_int, div_out))