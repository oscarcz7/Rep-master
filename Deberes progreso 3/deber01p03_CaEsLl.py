import numpy as np
from scipy import stats
from scipy.stats import binom
from scipy.stats import hypergeom
from scipy.stats import poisson
from scipy.stats import geom

#Ejercicio 1 
 #tasa de dispostivos defectuosos es de 3 % 

#Literal a

print("-----------------------------------------------")
print("Deber 01: Answer by simulation (discrete)")
print("Integrantes: Catota-Llangari-Escobar")
print("-----------------------------------------------")
print("Ejercicio 1, literal A)\n")

print ("X sigue una distribucion: b(x;20,0.03)")
print ("Entonces si P (X >= 1) = 1 - P(X = 0)")
print ("= 1 - b(0;20,0.03)")

n = 20 # articulos al azar 
p = 0.03  # 3% de dispositivos defectuosos
x = 0
size = 10000000
#calculo = 1 - binom.cdf(0,n,p)

calculo = binom.rvs(n,p,size=size)
a, b = np.unique(calculo, return_counts = True)

c = b/size
f = np.sum(c[1:])

print ("La probabilidad de que haya al menos un articulo defectuoso entre los 20 \ncon 10000000 de simulaciones es de:", f)
print("---------------------------------------------------")
print("Ejercicio 1, literal B)\n")

print("distribucion binomial de b (y, 10, 0.4562)")
print("Con: P(y = 3) y N = 10")

n2 = 10
calculo2 = binom.rvs(n2,f,size=size)
a2, b2 = np.unique(calculo2, return_counts = True)
c2 = b2/size

f2 = c2[3]

print("Probabilidad de que haya exactamente 3 cargamentos que contengan \nal menos un dispositivo defectuoso de entre los 20 seleccionados en 10000000 simulaciones es:" ,f2)

 #n = 5, N = 40, k = 3, x = 1 
print ("-----------------------------------------------------------------")
print ("Ejercicio 2)\n")

Mvar = 40
nvar = 5
Nvar = 3
print("Con, M = 40, n = 5 y N = 3:")
variable = hypergeom.rvs(Mvar, nvar, Nvar, size = size)
a3, b3 = np.unique(variable, return_counts = True)

c3 = b3/size
f3 = c3[1]

print ("Probabilidad de que se encuentre exactamente un componente defectuoso\ncon 10000000 de simulaciones:",f3)

print ("-----------------------------------------------------------------")
print ("Ejercicio 3)\n")

print("Con lambda = 1:")
z = poisson.rvs(1, size = size)

a4, b4 = np.unique(z, return_counts = True)

c4 = b4/size
poiss0 = (c4[0])
poiss1 = (c4[1])
poiss2 = (c4[2])
poiss3 = (c4[3])
poiss4 = (c4[4])
poiss5 = (c4[5])
poiss6 = (c4[6])

print ("para k(overflow floods in 100 years) = 0 con 10000000 simulaciones: ", poiss0)
print ("para k(overflow floods in 100 years) = 1 con 10000000 simulaciones: ", poiss1)
print ("para k(overflow floods in 100 years) = 2 con 10000000 simulaciones: ", poiss2)
print ("para k(overflow floods in 100 years) = 3 con 10000000 simulaciones: ", poiss3)
print ("para k(overflow floods in 100 years) = 4 con 10000000 simulaciones: ", poiss4)
print ("para k(overflow floods in 100 years) = 5 con 10000000 simulaciones: ", poiss5)
print ("para k(overflow floods in 100 years) = 6 con 10000000 simulaciones: ", poiss6)

print ("-----------------------------------------------------------------")
print ("Ejercicio 4)\n")

p2 = 0.05
# x = 5
print("Con p = 0.05 y x = 5:")
y = geom.rvs(p2, size = size)

a5, b5 = np.unique(y, return_counts = True)
c5 = b5/size

f5 = c5[4]
print ("Probabilidad de que se necesiten 5 intentos para enlazar \ncon exito una llamada en 10000000 simulaciones: ",f5)