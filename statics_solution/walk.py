import sys
import random
import matplotlib.pyplot as plt
import math

def Random_walk_2D( time ):

    x, y = 0, 0
    X = []
    Y = []
    D = []

    for _ in range( time ):

        x += random.choice( [-1,1] )
        y += random.choice( [-1,1] )

        X.append( x )
        Y.append( y )
        D.append( math.sqrt( (x*x) + (y*y) ) )

    return X, Y, D

if __name__ == "__main__":

    X, Y, D = Random_walk_2D( 10000 )

    plt.subplot( 1, 2, 1 )
    plt.plot( X, Y )
    plt.subplot( 1, 2, 2 )
    plt.plot( D )
    plt.show()

    

    