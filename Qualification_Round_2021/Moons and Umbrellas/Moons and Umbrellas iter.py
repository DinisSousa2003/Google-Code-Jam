# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:27:09 2021

@author: User
"""

T = int(input()) #number of test cases


def evaluate(X, Y, string):
    cost = 0
    for i in range(len(string) - 1):
        if string [i:i+2] == "CJ":
            cost += X
        if string [i:i+2] == "JC":
            cost += Y
    return cost


def iterPossibilities(alist, num_of_qmark):
    for i in range(num_of_qmark):
        num_elements_to_remove = len(alist)
        index = alist[0].index("?")
        for j in range(num_elements_to_remove):
            alist.append(alist[j][:index] + "C" + alist[j][index+1:])
            alist.append(alist[j][:index] + "J" + alist[j][index+1:])
        alist = alist[num_elements_to_remove:]
    return alist
    
    

def lowestWithIter(X, Y, string):
    alist = iterPossibilities([string], string.count("?"))
    return min(list(map(lambda x: evaluate(X, Y, x), alist)))

for i in range(T):
    L = input() #x y string
    L = L.split()
    X = int(L[0])
    Y = int(L[1])
    string = L[2]
    
    output = lowestWithIter(X, Y, string)
    
    print(f"Case #{i+1}: {output}")
        