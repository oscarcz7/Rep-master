import numpy as np
simulate = 1000


class Nodo:
    def __init__(self):
        self.position = np.array([0, 0])
        self.initial_position = np.array([0, 0])
        self.directions = {'up': np.array([0, 1]),
                           'down': np.array([0, -1]),
                           'right': np.array([1, 0]),
                           'left': np.array([-1, 0]),
                           
                           }

       
    def move(self):
        direction_ = ['up', 'down', 'right', 'left']
        np.random.shuffle(direction_)
        direction = direction_[0]
        self.position += self.directions[direction]

   

def is_origin(node):
    return np.array_equal(node.position, node.initial_position)



def walk_3d():
    flag = 0
    node = Nodo()
    while flag < 1000:
        flag += 1
        node.move()
        if is_origin(node):
            return True
    return False


node = Nodo()
success = 0
success2 = 0
for i in range(simulate):
    if walk_3d():
        success += 1
    

        
print('DEBER 03 P01 CATOTA - ESCOBAR - LLANGARI')
print('PROBABILITIES ')
print('The probability 3D walk', success/1000 )



