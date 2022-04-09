"""
Created on Wed Mar 16 15:39:11 2022

@author: bernardogoltz
@title: rede neural com múltiplas camadas de perceptrons, segundo encontro. 

x -ponderar pelos pesos>(normalizing func) -> y (result)

"""

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x)) 


a = np.random.randint(-10, 10, 10)

for i in range(len(a)):
    print("({}) -> {}".format(a[i] , sigmoid(i)))