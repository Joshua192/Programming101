#EXCERCISE 1
import random as rd
def mysqrt(x, eps):
    """Inputs:two numbers x, eps such that x >= 0, eps>=o
    Output: a number res such that x-eps <= res*res <= x+eps """
    g = rd.uniform(0, x)
    gsquared = g*g
    while(gsquared<x-eps or gsquared>x+eps):
        g = (g + x/g)/2 #new g is the average of g and x/g
        gsquared = g*g
    return g

# mysqrt(23,1.e-12)
# mysqrt(-23,1.e-12)  #Program does not end, maybe there's an exit condition not met?
#Stop the program and find out why error happened?
#How to feedback to user for case 2

# EXERCISE 2
def list_ratio(L1,L2):
    """Inputs: two lists L1 and L2 of equal sizes
    Output: a list ratios containing L1[i]/Li[2]"""
    ratios = []
    for i in range(len(L1)):
        ratios.append(L1[i]/L2[i])
    return ratios

# use inputs [3,6,-9] and [2,5,0]
#Note observations? or just check if the program fails and where
#Modify the code to work with the other input

#EXCERCISE 3
import random as rd
def mysqrt(x, eps):
    """Inputs:two numbers x, eps such that x >= 0, eps>=o
    Output: a number res such that x-eps <= res*res <= x+eps """
    g = rd.uniform(0, x)
    gsquared = g*g
    while(gsquared<x-eps or gsquared>x+eps):
        g = (g + x/g)/2 #new g is the average of g and x/g
        gsquared = g*g
    return g

# Add assertions to ensure inputs are non-negative
# Use exceptions to handle errors

try:
    f = open("toto.txt","r")
    fh = open(f)
    count = 0
    for line in f:
        count +=1
        print("Line count: ",count)
except FileNotFoundError:
    print("File does not exist!")
finally:
    f.close()

    #THIS CODE IS BUGGY, FIX IT