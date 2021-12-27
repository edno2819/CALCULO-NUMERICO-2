import numpy as np
from sympy import *
import Functions 



'''
Alfa_k = step size

- USAR O GRADIENTE DESCENDENTE
    * Use o método das diferenças finitas centradas: Usado para cálcular uma aproximação das derivadas

    * Golden Line: Uma variação do método Golden Section Search para achar o Alfa_k
    * Fibonacci
    * Método da pesquisa por divisão de intervalos
    * Função explicita de Alfa_k - Para função quadratica
'''


'''
DERIVADA:
DERIVADA EM UM PONTO: 
    x = var('x')
    x1 = var('x1')
    f = Lambda(x, (x**3 - 3*x + 2)*exp(-x/4) - 1)
    diff(f(x),x).subs(x,1)

DERIVADA COM 2 PARÂMETROS
    f2 = lambda x, x1: (x**4)+((x*x1**3)/3)

    DERIVADA PARCIAL EM X
        diff(f2(x,x1),x1)

    DERIVADA PARCIAL EM X1
        diff(f2(x,x1),x1)

    RESULTADO
        diff(f2(x,x1),x1).subs(x,1).subs(x1,2)

'''

def gradient_descent_derivada(func, init_value, iter=120, learning_rate=0.001):
    global X,Y
    x_new = init_value

    for i in range(iter):
        x_old = x_new
        x_new[0] = x_old[0] - learning_rate * diff(f2(X,Y), X).subs(Y, x_new[1]).subs(X, x_new[0])

    return x_new, func(*x_new) 


def diferenciais_finitas_centradas(x):...

def gradient_descent_derivada(func, init_value, iter=120, learning_rate=0.001):
    global X,Y
    x_new = init_value
    n = len(init_value)

    for i in range(iter):
        x_old = x_new
        x_new[0] = x_old[0] - learning_rate * diff(f2(X,Y), X).subs(Y, x_new[1]).subs(X, x_new[0])
        x_new[1] = x_old[1] - learning_rate * diff(f2(X,Y), Y).subs(X, x_new[0]).subs(Y, x_new[1])

    return x_new, func(*x_new) 

X = var('x')
Y = var('x1')
f2 = lambda X, Y: (X*X + Y - 11)**2 + (X + Y*Y - 7)**2#3,2

init_himmme =  [2, 5]

gradient_descent_derivada(f2, init_himmme)