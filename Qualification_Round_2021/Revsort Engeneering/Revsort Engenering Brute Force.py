# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:39:06 2021

@author: User
"""

import itertools

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

for j in range(T):
    INPUT = input() #SIZE, COST
    L = INPUT.split()
    L = list(map(lambda x:int(x), L))
    N = L[0]
    C = L[1]
    if C < N - 1 or C > sum(range(2, N+1)):
        print(f"Case #{j+1}: IMPOSSIBLE")
        continue
    possibilities = tuple((itertools.permutations((range(1, N+1)), N)))
    answer = ""
    for i in possibilities:
        i = list(i)
        cost = Revsort(i)
        if cost == C:
            answer = " ".join(list(map(lambda x:str(x), i)))
            break
    print(f"Case #{j+1}: {answer}")
    
    
