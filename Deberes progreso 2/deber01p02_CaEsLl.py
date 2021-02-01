import numpy as np
import matplotlib.pyplot as plt

print('Deber 01: Matching experiment')
print('Integrantes: Llangari-Catota-Escobar')
print('-- Se ha realizado 10000000 simulaciones para obtener el resultado esperado teoricamente --')
l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
l2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
a = []
rep = 10000000
def calculo():
    flag = 0
    while (flag < rep):
        np.random.shuffle(l1)
        np.random.shuffle(l2)
        rando = [i for i, j in zip(l1,l2) if i == j]
        x = len(rando)
        a.append(x)
        flag = flag + 1
   #print(a)
    print('-----------------------------------')
    print('Literal a:')
    print('-----------------------------------')
    veces0 = a.count(0)
    prob0 = veces0/rep
    print('Probabilidad de 0 parejas:',prob0)
    veces1 = a.count(1)
    prob1 = veces1/rep
    print('Probabilidad de 1 pareja :',prob1)
    veces2 = a.count(2)
    prob2 = veces2/rep
    print('Probabilidad de 2 parejas:',prob2)
    veces3 = a.count(3)
    prob3 = veces3/rep
    print('Probabilidad de 3 parejas:',prob3)
    veces4 = a.count(4)
    prob4 = veces4/rep
    print('Probabilidad de 4 parejas:',prob4)
    veces5 = a.count(5)
    prob5 = veces5/rep
    print('Probabilidad de 5 parejas:',prob5)
    veces6 = a.count(6)
    prob6 = veces6/rep
    print('Probabilidad de 6 parejas:',prob6)
    veces7 = a.count(7)
    prob7 = veces7/rep
    print('Probabilidad de 7 parejas:',prob7)
    veces8 = a.count(8)
    prob8 = veces8/rep
    print('Probabilidad de 8 parejas:',prob8)
    veces9 = a.count(9)
    prob9 = veces9/rep
    print('Probabilidad de 9 parejas:',prob9)
    veces10 = a.count(10)
    prob10 = veces10/rep
    print('Probabilidad de 10 parejas:',prob10)
    print('-----------------------------------')
    print('Literal b:')
    print('-----------------------------------')
    media = np.mean(a)
    print('Media: ',media)
    varianza = np.var(a)
    print('Varianza: ',varianza)
    print('------------------------------------')
    print('Literal c:')
    print('------------------------------------')
 
    sumatoriaT = (veces3 + veces4 + veces5 + veces6 + veces7 + veces8 + veces9 + veces10)/rep 
    print('Probabilidad de al menos 3 matches:')
    return sumatoriaT
print(calculo())
