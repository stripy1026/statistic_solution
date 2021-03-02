import sys
import random
import math
import matplotlib.pyplot as plt

def Make_2D_list( row ):

    lattice = []
    for _ in range( row ):

        lattice.append( [0]*row )

    return lattice

def Calculate_dE_2D( lattice, x, y ):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    Neighbor_spin_value = 0

    for i in range( 4 ):

        X = x + dx[i]
        Y = y + dy[i]
        
        if X < 0:

            X = len( lattice ) - 1

        if X >= len( lattice ):

            X = 0

        if Y < 0:

            Y = len( lattice ) - 1

        if Y >= len( lattice ):

            Y = 0

        Neighbor_spin_value += lattice[X][Y]
    
    Neighbor_spin_E = (-2)*Neighbor_spin_value

    return Neighbor_spin_E

def Move_spin( lattice, x, y, E, T ):

    r = random.random()
    p = math.exp( (-E)/T )

    if r > p:

        lattice[x][y] *= -1

    return

if __name__ == "__main__":

    #####################################

    row_size = 10
    Temperature_range = 5

    #####################################

    Temperature_list = []
    Magnetization_list = []

    lattice = Make_2D_list( row_size )

    for _ in range( 1000 ):

        for i in range( row_size ):

            for j in range( row_size ):

                lattice[i][j] = random.choice( [-1,1] )

        T = ( random.random() )*Temperature_range
        Temperature_list.append( T )    

        for _ in range( 10000 ):

            x = random.randrange( row_size )
            y = random.randrange( row_size )

            lattice[x][y] *= -1

            dE = Calculate_dE_2D( lattice, x, y )
                    
            if lattice[x][y] < 0:

                dE *= -1

            if dE >= 0:

                Move_spin( lattice, x, y, dE, T )


        M = 0
        
        for i in range( row_size ):

            for j in range( row_size ):

                M += lattice[i][j]
        
        Magnetization_list.append( M/100 )

    plt.plot( Temperature_list, Magnetization_list, 'o' )
    plt.show()



                        

                        












    






