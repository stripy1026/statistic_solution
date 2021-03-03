from walk import *
import matplotlib.pyplot as plt

def Ensemble( t, time ):

    SX = [0]*time
    SY = [0]*time
    SD = [0]*time

    for _ in range( t ):

        X, Y, D = Random_walk_2D( time )

        for i in range( time ):

            SX[i] += X[i]
            SY[i] += Y[i]
            SD[i] += D[i]
        
        plt.subplot( 2, 2, 1 )
        plt.plot( X, Y )
        plt.subplot( 2, 2, 2 )
        plt.plot( D )

    for i in range( time ):

        SX[i] /= t
        SY[i] /= t
        SD[i] /= t

    plt.subplot( 2, 2, 3 )
    plt.plot( SX, SY )
    plt.subplot( 2, 2, 4 )
    plt.plot( SD )
    
    plt.show()

Ensemble( 100, 10000 )