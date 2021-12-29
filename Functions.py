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

   
class Quadatic_explicit:
    Q = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
    b = np.array([11, 12, 10])
        
    def getGradiente(self, x):
        x = np.array(x)
        return ((x)@self.Q - self.b)
    
    def get_delta_k(self, x, gk):
        x = np.array(x)
        d = (gk@np.transpose(gk))
        q = (gk@(self.Q@np.transpose(gk)))

        return d/q

    def passo(self, x, g):
        return np.array(g)*self.get_delta_k(x, g)

    def new_x(self, x, g):
        return x - self.passo(x, g)

    def funcaoQuadratica(self, x):
        x = [x]
        a = x@(self.Q@(np.transpose(x)*0.5))
        b = x@np.transpose(self.b)
        return abs(float((a-b)))

    def funcaoQuadratica_args(self, x, y, z):
        x = [x, y, z]
        a = x@(self.Q@(np.transpose(x)*0.5))
        b = x@np.transpose(self.b)
        return float(a-b)



'''
Q = Hessiana da função
deltaf(x) = Gradiente da função
g0 = deltaf(x0) 
'''
