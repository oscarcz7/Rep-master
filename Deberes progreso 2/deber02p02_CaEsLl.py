'''
Deber 02: Generating random variables (discrete)
Responda por simulación:

El propietario de un puesto de periódicos recibe 50 ejemplares del periódico El Uninverso cada mañana. La cantidad de ejemplares demandados, X, varía al azar de acuerdo con la siguiente distribución de probabilidad:

f(x)=⎧⎩⎨⎪⎪⎪⎪145,130,133,x=35,36,...,49x=50,51,...59x=60,61,...70

Determine la probabilidad de que el propietario venda todos los ejemplares.
Determine el número esperado de ejemplares no vendidos por día.
Un ejemeplar cuesta 50 centavos y se vende a $1.00. Determine el ingreso neto esperado por día.
'''
import numpy as np

print('------------------------------------------------------')
print('Deber 02: Generating random variables (discrete)')
print('Integrantes: LLANGARI-CATOTA-ESCOBAR')
print('------------------------------------------------------')
rep = 10
a = []
b = []
def SellAll():
    flag1 = 0

    while (flag1 < rep):
        no_sell = 50 - np.array(range(35, 71))
        no_sell[np.where(no_sell < 0)[0]] = 0
        px = np.concatenate((np.ones(50-35)*1/45, np.ones(60-50)*1/30, np.ones(71-60)*1/33))
        pos_all_sell = np.where(no_sell == 0)[0]
        probsellAll = np.sum(px[pos_all_sell])
        a.append(probsellAll)
     
        no_sell_sim = np.random.choice(no_sell, p=px)
        b.append(no_sell_sim)
        flag1 = flag1 + 1

    severithing = np.sum(a)/rep
    nosellever = np.sum(b)/rep
    sold = 50 - nosellever
    ganancias = sold * 1 - 50*0.50
    print(a)
    print(no_sell)
    print(pos_all_sell)
    #print(b)
    print('1. Probabilidad de que el propietario venda todos los ejemplares en 10000 simulaciones:', severithing)
    print('2. Numero promedio esperado de ejemplares no vendidos por dia en 10000 simulaciones:', nosellever)
    print('3. Ingreso promedio neto esperado por dia con 10000 simulaciones: ', ganancias)

SellAll()





