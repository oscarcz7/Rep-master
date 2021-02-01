import numpy as np 
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
print('Deber 03:Develop a random-variate generator for a random variable X with the pdf')
print('Integrantes: Catota-Escobar-LLangarí')
########################################################################################################
#               1.Develop a random-variate generator for a random variable X with the pdf              #
########################################################################################################

 #######################################
 #       Definición de Funciones       #
 #######################################
def f(x):
    return np.e**(2*x);  # evaluamos fx

def f2(x):
    return np.e**(-2*x);  # evaluamos fx

x = np.linspace(-5, 0, 100)  
fx = f(x)  
x2 = np.linspace(0, 5, 100)  
fx2 = f2(x2)  

print("Ejercicio 1:")
print("Area f1:",np.trapz(f(x),x))
print("Area f2:",np.trapz(f2(x2),x2))
print("\n")

 ############################################################################
 #                      Inverse Transform Sampling                          #
 ############################################################################
size = 100000
U = np.random.rand(size)  # Uniform distribution sampling
AU=[]
#Inversa f1:  ln(2x)/2
#Inversa f2:  -ln(-2x)/2
#U < 0.5  # U distr. uniforme U(0,1)
#I1(U) else I2(U)  # I inversa de la acumulada

for i in range(len(U)):
    u=U[i]
    
    if(u<0.5):
         I1=(np.log(2*u))/2
         AU.append(I1)    
    else:
         I2=(-np.log((-2*u)+2))/2
         AU.append(I2)    

#print("AU",AU)
plt.figure()
fig = plt.gcf()
fig.canvas.set_window_title('Ejercicio 3')


plt.subplot(2,2,1)
plt.plot(x,f(x),linewidth=3)
plt.plot(x2,f2(x2),linewidth=3)
plt.title("Inverse Transform Sampling")
plt.hist(AU,density=True,facecolor='red', edgecolor='black',bins=100)

############################################################################
#                          Rejection Method                                #
############################################################################

size = 100000

(a, b, c) = (-5, 0, 1)
(a2, b2, c2) = (0, 5, 1)

A = []
B = []

i = 0
j=0
while i < size:
    x_r = a + (b - a) * np.random.rand()
    y_r = c * np.random.rand()

    if y_r < f(x_r):  
        A += [x_r]  
        i += 1
               
while j < size:
    x2_r = a2 + (b2 - a2) * np.random.rand()
    y2_r = c2 * np.random.rand()

    if y2_r < f2(x2_r):  
        B += [x2_r]  
        j += 1
        
X=np.concatenate((A, B), axis=None)

plt.subplot(2,2,2)
plt.plot(x, f(x))
plt.plot(x2, f2(x2))
plt.title("Rejection Method")
plt.hist(X,density=True,facecolor='green', edgecolor='black',bins=100)

########################################################################################################
#                   2.Develop a generation scheme for the triangular distribution with pdf             #                                               #
########################################################################################################
#######################################
#       Definición de Funciones       #
#######################################

def f(x):
    return 1/2 * (x-2)

def f2(x):
    return 1/2 * (2-x/3)

x = np.linspace(2, 3, 100)
fx = f(x)  
x2 = np.linspace(3, 6, 100) 
fx2 = f2(x2)  

area1 = round(np.trapz(fx, x),2)
area2=round(np.trapz(fx2, x2),2)

print("Ejercicio 2:")
print("El área es:",area1)
print("El área es:",area2)
############################################################################
#                      Inverse Transform Sampling                          #
############################################################################
a=2
b=6
c=3
size = 100000
U1 = np.random.rand(size) 

AU1=[]

#I1= a + np.sqrt((b-a)*(c-a)*u)
#I2= b - np.sqrt((b-a)(b-c)(1-u))

for i in range(len(U)):
    u=U1[i]
    
    if (u < 0.25):
         I1=(a + (np.sqrt((b-a)*(c-a)*u)))
         AU1.append(I1)    
    else:
         I2=(b - (np.sqrt((b-a)*(b-c)*(1-u))))
         AU1.append(I2)    

plt.subplot(2,2,3)
plt.plot(x,f(x),linewidth=3)
plt.plot(x2,f2(x2),linewidth=3)
plt.title("Inverse Transform Sampling")
plt.hist(AU1,density=True,facecolor='red', edgecolor='black',bins=100)


############################################################################
#                          Rejection Method                                #
############################################################################

size = 1000000

(a, b, c) = (2, 6, 0.5)

D = []
D1 = []
E = []
E1 = []


j=0

    
               
while j < size:
    x_r = a + (b - a) * np.random.rand()
    y_r = c * np.random.rand()
    
    if y_r < f2(x_r) and y_r < f(x_r):  
        E += [x_r]  
        E1 += [y_r] 

        D += [x_r]   
        D1 += [y_r] 
         
        j += 1

#print('E',E)        
#print('E1',E1)        
W=np.concatenate((E,D), axis=None)
Z=np.concatenate((E1,D1), axis=None)

plt.subplot(2,2,4)
#plt.plot(W,Z,'.')
plt.plot(x, f(x))
plt.plot(x2, f2(x2))
plt.title("Rejection Method")
plt.hist(W,density=True,facecolor='green', edgecolor='black',bins=100)
plt.show()







