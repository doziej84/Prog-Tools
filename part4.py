# -*- coding: utf-8 -*-
"""
function that takes natural number and returns the divisors
"""

nat_num=int(input("Enter an integer:"))

print("The divisors of the natural number are:")

for i in range(1, nat_num):
    if(nat_num%i==0):
        print(i)