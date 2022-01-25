# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:00:30 2022

@author: Admin
"""

import math

def divisor(n):
    list = []
    int = 1
    while int <= n/2:
        if (n %  int == 0):
            list.append(int)
        int += 1
    return list

num_divisor= divisor(100)
print(num_divisor)