# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


#numrandom = np.random.randint(10000,100000)/100000
p = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
formula = p**2*(2-p**2)
print('Ejercicio #4 - 2 by 2 Percolation')
print('Integrantes: Catota-Llangari-Escobar')
print('---------------------------------------------------------------')
print('Probabilidad teorica de valores entre 0.1 a 0.9:',formula)

##PROBABILIDAD 0.1
def prob():
    graf = np.random.choice([0, 1], p=[0.1,0.9], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.1:')
print(Simulacion())

##PROBABILIDAD 0.2
def prob():
    graf = np.random.choice([0, 1], p=[0.2,0.8], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.2:',simulacion())

##PROBABILIDAD 0.3
def prob():
    graf = np.random.choice([0, 1], p=[0.3,0.7], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.3:',simulacion())

##PROBABILIDAD 0.4
def prob():
    graf = np.random.choice([0, 1], p=[0.4,0.6], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.4:',simulacion())


##PROBABILIDAD 0.5
def prob():
    graf = np.random.choice([0, 1], p=[0.5,0.5], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == x) and (graf[1][0] == x) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.5:',simulacion())

##PROBABILIDAD 0.6
def prob():
    graf = np.random.choice([0, 1], p=[0.6,0.4], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.6:',simulacion())

##PROBABILIDAD 0.7
def prob():
    graf = np.random.choice([0, 1], p=[0.7,0.3], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == x) and (graf[1][0] == x) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.7:',simulacion())

##PROBABILIDAD 0.8
def prob():
    graf = np.random.choice([0, 1], p=[0.8,0.2], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == x) and (graf[1][0] == x) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.8:',simulacion())

##PROBABILIDAD 0.9
def prob():
    graf = np.random.choice([0, 1], p=[0.9,0.1], size = (2,2))
    #print(graf)
    #plt.matshow(graf)
    #plt.show()
    x = 1
    y = 0
    if (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == x) and (graf[1][0] == x) and (graf[1][1] == x):
        return 1
    elif (graf[0][0] == x) and (graf[0][1] == y) and (graf[1][0] == x) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == x) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1    
    elif (graf[0][0] == y) and (graf[0][1] == y) and (graf[1][0] == y) and (graf[1][1] == y):
        return 1
    else:
        return 0

rep = 100
def perRange(rep):
    per = [prob() for i in range(rep)]
    return np.sum(per)

def calculo():
    probabilidad = perRange(rep)/rep
    return probabilidad

def simulacion():
     sim = 1000
     simul = [calculo() for i in range (sim)]
     a = (np.sum(simul))
     b = a/sim
     return b

print('Probabilidad simulada 1000 veces para 0.9:',simulacion())

plt.plot(p, formula, ':.')
plt.title("Representacion grafica probabilidad 0.1 a 0.9")
plt.show()