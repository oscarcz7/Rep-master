import numpy as np
import matplotlib.pyplot as plt
import random
import collections

sim = 1000


def walk(x_grid=9, y_grid=9, figure=False):
    # Dictionary of movements
    mov = {0: (0, -1), 1: (0, 1), 2: (1, 0), 3: (-1, 0)}
    walk = [[0, 0]]
    walkA = []
    cont = acum = 0

    # Grid Limits
    x_pos = np.floor(x_grid / 2) + 1
    x_neg = -(np.floor(x_grid / 2) + 1)
    y_pos = np.floor(y_grid / 2) + 1
    y_neg = -(np.floor(y_grid / 2) + 1)

    # Random walk generation w
    while acum != 4:
        step = []
        n = random.randint(0, 3)
        step += [[walk[-1][0] + mov[n][0], walk[-1][1] + mov[n][1]]]
        # condition if step is in walk to increment acum
        if step[0] not in walkA:
            walkA.append(step[0])
            acum += 1
        # Condition if step not in walk
        if step[0] not in walk:
            # condition to probe that the trace dont pass the limits
            if (step[0][0] != x_pos and step[0][0] != x_neg) and (step[0][1] != y_pos and step[0][1] != y_neg):
                walk.extend(step)
                acum = 0
                walkA = []
                cont += 1
    # generation of the walk
    x = []
    y = []
    for e in walk:
        x += [e[0]]
        y += [e[1]]
    # drawing the figure
    if figure:
        plt.figure(1)
        plt.title('RANDOM WALK')
        plt.plot(x, y)
        plt.xlim(x_pos, x_neg)
        plt.ylim(y_pos, y_neg)
        plt.grid()
        plt.gca().set_aspect('equal', adjustable='box')

    return cont


# function to create the simulation of the walk and count the steps
def simulation(x_grid, y_grid, numSim):
    n = 0
    for _i in range(numSim):
        cont = walk(x_grid, y_grid)
        n += cont
    n = n / numSim
    return n


# refers to simulation and the grid size
def responses():
    tam = []
    tam1 = []
    tam3 = []
    plt.figure(2, figsize=(10, 6))
    for _axisLen in range(3, 10):
        n = simulation(_axisLen, _axisLen, sim)
        plt.plot(_axisLen, n, '*', markersize=20)
        tam.append(n)
    for _i in range(1, 7):
        tam3 += [tam[_i] - tam[_i - 1]]
    evaluation = sum(tam3) / len(tam3)

    plt.xlabel('GRID LEN')
    plt.ylabel('MEDIA EXECUTION')
    plt.yticks(tam, tam)
    plt.grid()

    for _iterable in range(sim):
        tam1 += [walk()]
    tam1.sort()
    count1 = collections.Counter(tam1)

    # Print of the data calculated
    print('DEBER 01 P01 CATOTA - ESCOBAR - LLANGARI \n')
    print(('RANDOM WALK\n'))
    print('Median grid size 9*9 -->', simulation(9, 9, sim))
    print('\n')
    print('median of steps evaluated in the grid tam -->', evaluation)
    print('\n')
    print('Steps quantity collection elements repeated --v')
    print('\n')
    print(count1)

    plt.figure(3)
    plt.title('STEP DISTRIBUTION')
    plt.hist(tam1, bins=60, edgecolor='red', linewidth=0.5)
    plt.xlabel('STEPS QUANTITY')
    plt.ylabel('FREQUENCY')


# functions call
walk(figure=True)
responses()
plt.show()
