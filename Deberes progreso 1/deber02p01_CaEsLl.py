# -*- coding: utf-8 -*-
import random 
import numpy as np 
import matplotlib.pyplot as plt 

print('Ejercicio #2 - Random Walk 5%')
print('Integrantes: Catota-Escobar-Llangari')
print('---------------------------------------------------------')

def walk():
    m=10   #Absorbing Barrier
    x=[0]  #Start
    sum=0  #Number of steps counter
    while(x[-1]!=m):
        n=np.random.choice([-1,1],p=[0.5,0.5])
        if(x[-1]==0):
            x += [x[-1]+1]        
        else:
            if(x[-1]!=0):
                x += [x[-1]+n]
    sum=len(x)-1
    print(x)
    print("Steps:",sum)
    print("Analytic solution:",m**2)
    plt.plot(x)
    return sum



def main ():
    
    numSim=1000 #Number of simulations
    count=0   #Total number of steps 
    for i in range(numSim):
        print("\nSimulation #",i+1)
        count+=walk()
      
    
    print("----------------------------\nTotal:",count)
    print("Mean :",count/numSim)
    
   
    plt.title("Ejercicio 2: Random Walk 5%")
    plt.show()
main()



