# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:59:37 2021

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
def recPossibilities(alist):
    no_change = True
    for string in alist:
        for i in range(len(string)):
            if string[i] == "?":
                no_change = False
                alist.append(string[:i] + "C" + string[i+1:])
                alist.append(string[:i] + "J" + string[i+1:])
                alist.remove(string)
                break
    if no_change:
        return alist
    else:
        return recPossibilities(alist)
#####
def lowest(X, Y, string):
    alist = recPossibilities([string])
    return min(list(map(lambda x: evaluate(X, Y, x), alist)))
    

for i in range(T):
    L = input() #x y string
    L = L.split()
    X = int(L[0])
    Y = int(L[1])
    string = L[2]
    
    output = lowest(X, Y, string)
    
    print(f"Case #{i+1}: {output}")
        


    