import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
from random import gauss

print('DEBER 02 - CATOTA / ESCOBAR / LLANGARI')
print('-------------------------------------------')
def literal1():
    arr1=[]
    arr2=[]
    flag =0
    Ep = 0
    bid = 0
    mProfit = 0
    simulation = 100000
    #x.sort()
    x = np.linspace(100000,140000, 60, dtype=int)
    #print (x)
    for i in range(len(x)):
        profit = 0
        for j in range(simulation):
            xC = np.random.randint(70000, 140000)
            if xC > x[i]:
                profit += x[i] - 100000
            
        Ep = profit/simulation
        if(Ep>0):
            arr1.append(Ep)
            arr2.append(x[i])
            if(Ep > mProfit):
                mProfit = Ep
                bid = x[i]
            
            
    #print('arreglo2', arr2)
    print('DEBER 02 - LITERAL 01 ')
    #print('Oferta', x)
    print(' ')
    print('BEST BID', bid)
    print(' ')
    print('MAX PROFIT', mProfit  )
    
    plt.subplot(2,1,1)
    plt.plot(arr2,arr1, color='green', linestyle='dashed', linewidth= 1, marker='o', markerfacecolor='blue', markersize=3)      
   
    plt.xlabel('Oferta')
    plt.ylabel('Utilidad_Esperada')
    


def literal2() :
    simulation = 1000000
    percentage = 0
    minutes = 0
    arr1 =[]
    mu, sigma = 40, 7 # media y variacion estandar
    normal = stats.norm(mu, sigma)
    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
    fp = normal.pdf(x)
    prob = np.max(fp)
    fx= x - 40 / 7
    val= 1.645
    t = (val *7 ) + 40 ##51.52
    seg, min = math.modf(t)
    ##################################################33
    tiempo= np.random.randint(1, 60, size=30)
    for a in tiempo:
        arrive=0
        for b in range(simulation):
            if(gauss(40, 7) < a):
                arrive += 1
        arr1.append(arrive/simulation)
        if (arrive / simulation >= 0.95 ):
            
            minutes=  a
    print('-------------------------------------------')
    print('DEBER 02 - LITERAL 02')
    print(' ')
    print('THEORICAL ANSWER')
    print ('MAXIMUN TIME TRAVEL', t)
    print(' ')
    print('SIMULATED ANSWER')
    print ('SIMULATION MAX TIME TRAVEL ', minutes)
   

    plt.subplot(2,1,2)
    plt.plot(x, fp)
    #plt.title('Distribución Normal')
    plt.ylabel('Probabilities')
    plt.xlabel('Values')
   

literal1()
literal2()
plt.show()



