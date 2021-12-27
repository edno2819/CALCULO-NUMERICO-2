import numpy as np 


def rosen(x:list): 
    return np.sum(100*(x[1:][0]-x[:-1][0]**2)**2 + (1-x[:-1][0])**2, axis=0) 


def rosenbrock(X:list):
    x = X[0]
    y = X[1]
    a = 1. - x
    b = y - x*x
    return a*a + b*b*100.


def himmelblau(X):
    x = X[0]
    y = X[1]
    a = x*x + y - 11
    b = x + y*y - 7
    return a*a + b*b


def quadratica_QP(x):
    x = np.array(x).reshape(3,3)
    Q = [[2,-1,0],[-1,2,-1],[0,-1,2]]
    b = [11, 12, 10]
    result = (0.5*np.transpose(x)) * (Q@x) - (np.transpose(b)@x)
    return result.reshape(1,9)[0]


#quadratica_QP([[2,2,5],[1,2,3],[0,6,3]])