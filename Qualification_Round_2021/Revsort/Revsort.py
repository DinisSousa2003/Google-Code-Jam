# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:26:54 2021

@author: User
"""

T = int(input()) #"Number of test cases"


def lower_pos(L):
    a = min(L)
    return L.index(a)

def Revsort(L):
    cost = 0
    for i in range(0, len(L) - 1):
        j = lower_pos(L[i:len(L)]) + i
        mid_part = Reverse(L[i:j+1])
        L =  L[:i]+ mid_part + L[j+1:]
        cost += j - i + 1
    return cost
        
def Reverse(L):
    L.reverse()
    return L

for i in range(T):
    N = int(input()) #"lenght"
    L = input() #numbers
    L = L.split()
    L = list(map(lambda x:int(x), L))
    cost = Revsort(L)
    print(f"Case #{i+1}: {cost}")
    
    

