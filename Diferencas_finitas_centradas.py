import random
import numpy as np
from sympy import *


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p


def diferencas_finitas(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        A.append([0] * n)

        for j in range(n):
            A[i][j] = xs[j] ** i

        potencias = [k +1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial *x0 **(i - ordem)
        B.append(termo)

    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)

    soma = 0
    for c, x in zip(cs, xs):
        soma += c *f(x)


    return  soma


def derivada_parcial(f, args, ponto, num_pontos, index_var):
    def new_f(var):
        args[index_var] = var
        return f(*args)
        
    ordem = 1
    a = ponto - 0.25
    b = ponto + 0.25
    xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
    xs.sort()
    r = diferencas_finitas(xs, ordem, ponto, new_f)
    #print(f'Aproximação de f NO PONTO {ponto} é: {r}')
    return r

'''
 - Teste

    x = var('x')
    y = var('y')
    z = var('z')
    f2 = lambda x, y, z: (x**3)+7*y-4+z*y

    diff(f2(x,y,z), y).subs(x, 2).subs(z, 5).subs(y, 3)
    derivada_parcial(f2, [2,y,5], 3, 25, 1)

'''