# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:39:48 2022

@author: johnf
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("ex2data1.txt",names=["x1","x2","y"])
df.info()
plt.scatter(df["x1"],df["x2"],c=df["y"])


theta=np.array([-25,0,10])

x1=np.arange(0,100)
x2=(-theta[1]*x1/theta[2]-theta[0]/theta[2])
#theta[1]*x1-theta[2]*x2
plt.plot(x1,x2,"k")

X1=df["x1"]
X2=df["x2"]
y=df["y"]
h=1/(1+np.exp(-theta[0]*1-theta[1]*X1-theta[2]*X2))

m=len(X1)
alfa=0.001
lamb=0

for i in range(5000):  
    theta=theta-alfa/m*(np.array([sum((h-y)*1),sum((h-y)*X1),sum((h-y)*X2)])+lamb/m*theta)
    h=1/(1+np.exp(-theta[0]*1-theta[1]*X1-theta[2]*X2))
    #hg=1/(1+np.exp(-theta[0]-theta[1]*xg))
    #g,=plt.plot(xg,hg,"b")
    x2=(-theta[1]*x1/theta[2]-theta[0]/theta[2])
    #theta[1]*x1-theta[2]*x2
    g,=plt.plot(x1,x2,"r")

    plt.pause(0.001)
    g.remove()
    #print(theta)
print(theta)


x1=np.arange(0,100)
x2=(-theta[1]*x1/theta[2]-theta[0]/theta[2])
#theta[1]*x1-theta[2]*x2
plt.plot(x1,x2,"r")


