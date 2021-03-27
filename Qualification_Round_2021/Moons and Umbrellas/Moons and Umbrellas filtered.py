# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:59:00 2021

@author: User
"""

T = int(input()) #number of test cases

#WORKING NICELY
def evaluate(X, Y, string):
    cost = 0
    for i in range(len(string) - 1):
        if string [i:i+2] == "CJ":
            cost += X
        if string [i:i+2] == "JC":
            cost += Y
    return cost

#####
def lowest(X, Y, string):
    l = list(filter(lambda x:x!="?", string))
    string = "".join(l)
    cost = evaluate(X, Y, string)
    return cost

for i in range(T):
    L = input() #x y string
    L = L.split()
    X = int(L[0])
    Y = int(L[1])
    string = L[2]
    
    output = lowest(X, Y, string)
    
    print(f"Case #{i+1}: {output}")
        