import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from tabulate import  tabulate
from scipy.stats import norm
from scipy.stats import uniform
from scipy.stats import t

print("-----------------------------------------------")
print("Deber 03: Sampling distributions")
print("Integrantes: Catota-Escobar-Llangari")
print("-----------------------------------------------")

table = [
["5","5.1 %","6.6 %","11.6 %","3.3 %"],
["20","4.9 %","5.2 %","8.1 %","3.7 %"],
["50","5.0 %","5.2 %","6.5 %","3.9 %"],
["100","5.0 %","4.9 %","5.7 %","4.2 %"]]
print(tabulate(table,headers=["n","Normal","Uniforme","Exponencial","Colas Pesadas"],tablefmt="grid"))
#######################################################################################
#                            Distribución Normal                                      #
#######################################################################################
print("Resultados:")
p_values = []
for simul in range(10000):
    rvs = stats.norm.rvs(loc=5, scale=10, size=(5))
    p_values += [stats.ttest_1samp(rvs,5.0)[1]]

n5=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#print("n=5 -->",n5)
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.norm.rvs(loc=5, scale=10, size=(20))
    p_values += [stats.ttest_1samp(rvs,5.0)[1]]

n20=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#print("n=20 -->",n20)

#######################################################################################

p_values = []
for simul in range(10000):
    rvs =norm.sf(loc=5, scale=10, size=(50))
    p_values += [stats.ttest_1samp(rvs,5.0)[1]]

n50=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#print("n=50 -->",n50)

#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.norm.rvs(loc=5, scale=10, size=(100))
    p_values += [stats.ttest_1samp(rvs,5.0)[1]]

n100=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#print("n=100 -->",n100)

#######################################################################################
#                            Distribución Uniforme                                    #
#######################################################################################
p_values = []
for simul in range(10000):
    rvs = stats.uniform.rvs(loc=0, scale=40, size=(5))
    p_values += [stats.ttest_1samp(rvs,20)[1]]

u5=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'

#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.uniform.rvs(loc=0, scale=40, size=(20))
    p_values += [stats.ttest_1samp(rvs,20)[1]]

u20=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'

#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.uniform.rvs(loc=0, scale=40, size=(50))
    p_values += [stats.ttest_1samp(rvs,20)[1]]

u50=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'

#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.uniform.rvs(loc=0, scale=40, size=(100))
    p_values += [stats.ttest_1samp(rvs,20)[1]]

u100=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'

#######################################################################################
#                            Distribución Exponencial                                 #
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.expon.rvs(loc=0, scale=5, size=(5))
    p_values += [stats.ttest_1samp(rvs,5)[1]]

e5=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.expon.rvs(loc=0, scale=5, size=(20))
    p_values += [stats.ttest_1samp(rvs,5)[1]]

e20=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.expon.rvs(loc=0, scale=5, size=(50))
    p_values += [stats.ttest_1samp(rvs,5)[1]]

e50=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################
p_values = []
for simul in range(10000):
    rvs = stats.expon.rvs(loc=0, scale=5, size=(100))
    p_values += [stats.ttest_1samp(rvs,5)[1]]

e100=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################
#                       Distribución de Colas Pesadas                                 #
#######################################################################################
p_values = []
for simul in range(10000):
    rvs = stats.t.rvs(df=2,size=(5))
    p_values += [stats.ttest_1samp(rvs,0)[1]]

h5=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.t.rvs(df=2,size=(20))
    p_values += [stats.ttest_1samp(rvs,0)[1]]

h20=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.t.rvs(df=2,size=(50))
    p_values += [stats.ttest_1samp(rvs,0)[1]]

h50=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################

p_values = []
for simul in range(10000):
    rvs = stats.t.rvs(df=2,size=(100))
    p_values += [stats.ttest_1samp(rvs,0)[1]]

h100=str(100*(len(np.where(np.array(p_values) < 0.05)[0])/len(p_values)))+' %'
#######################################################################################
table2 = [
["5",n5,u5,e5,h5],
["20",n20,u20,e20,h20],
["50",n50,u50,e50,h50],
["100",n100,u100,e100,h100]]
print(tabulate(table2,headers=["n","Normal","Uniforme","Exponencial","Colas Pesadas"],tablefmt="grid"))


