import numpy as np
import Functions 
import copy
from Diferencas_finitas_centradas import *



'''
Alfa_k = step size

- USAR O GRADIENTE DESCENDENTE
    * Use o método das diferenças finitas centradas: Usado para cálcular uma aproximação das derivadas

    * Golden Line: Uma variação do método Golden Section Search para achar o Alfa_k
    * Função explicita de Alfa_k - Para função quadratica
'''

def Golden_Line(func_var,  x, search, a=-10, b=10,   maxiter=100, epsilon=0.0002):
        tau = 0.381967
        x = np.array(x)
        search = np.array(search)
        alpha1 = a*(1-tau) + b* tau
        alpha2 = a* tau + b*(1-tau)
        falpha1 = func_var(*(x + alpha1 * search))
        falpha2 = func_var(*(x + alpha2 * search))
        for k in range(1,maxiter):

                if (falpha1 > falpha2):
                        a = alpha1
                        alpha1 = alpha2
                        falpha1 = falpha2
                        alpha2 = tau*a + (1-tau)*b
                        falpha2 = func_var(*(x+alpha2 * search))

                else:
                        b = alpha2
                        alpha2 = alpha1
                        falpha2 = falpha1
                        alpha1 = tau*b + (1-tau)*a
                        falpha1 = func_var(*(x+alpha1 * search))

                if (abs(func_var(*(x+alpha1 * search)) - func_var(*(x+alpha2 * search)))< epsilon):
                        break
        alpha1 = alpha1 if alpha1<alpha2 else alpha2              
        return (alpha1 , falpha1)


def gradient_descent_derivada(func, init_value, iter=100, learning_rate=0.001, verbose=False):
    VAR = [0,0,0]
    x_new = init_value
    n = len(init_value)

    for i in range(iter):
        x_old = x_new
        for var in range(n):
            variavel = VAR[var]
            args = copy.deepcopy(x_old)
            args[var] = variavel
            gradiente = derivada_parcial(func, args, x_old[var], 25, var)
            x_new[var] = x_old[var] - learning_rate * gradiente

            resu = func(*x_new)
            if verbose:
                print(f'Iteração {i} / Result: {resu}')
            if resu<0.02:
                break

    print(f'Valor da função otimizada: {func(*x_new)}')
    print(f'Valor das variáveis: {x_new}')


def gradient_descent_Golden_Line(func, init_value, iter=50, verbose=False):
    VAR = [0,0,0]
    x_new = init_value
    n = len(init_value)

    for i in range(iter):
        x_old = x_new

        derivadas_parciais = []
        for var in range(n):
            variavel = VAR[var]
            args = copy.deepcopy(x_old)
            args[var] = variavel
            derivadas_parciais.append(derivada_parcial(func, args, x_old[var], 25, var))

        alpha, _  = Golden_Line(func, x_old, derivadas_parciais)
        x_new = x_old + alpha * np.array(derivadas_parciais)

        resu = func(*x_new)
        if verbose:
            print(f'Iteração {i} / Result: {resu}')


    print(f'Valor da função otimizada: {func(*x_new)}')
    print(f'Valor das variáveis: {x_new}')


def gradient_descent_QD(func, init_value, iter=50, verbose=False):
    global t

    x = init_value
    g = t.getGradiente(x)

    for i in range(iter):
        x = t.new_x(x, g)   
        g = t.getGradiente(x)
        resu = func(x)

        if verbose:
            print(f'Iteração {i} / Result: {resu}')

    print(f'Valor da função otimizada: {func(x)}')
    print(f'Valor das variáveis: {x}')



himmelblau = lambda x, y: (x*x + y - 11)**2 + (x + y*y - 7)**2
rosenbrock = lambda x, y: np.sum(100*(y-x**2)**2 + (1-x)**2, axis=0) 
t = Functions.Quadatic_explicit()

init_himmme =  [.5, .5]
init_rosen =  [6, .5]
init_quadatic = [10, 10, 10]

print('Minimização usando Golden Line\n')

print(f'\n----- Minimizando Himmelbalu')
gradient_descent_Golden_Line(himmelblau, init_rosen, 16, verbose=True)

print(f'\n----- Minimizando Rosenbrock')
gradient_descent_Golden_Line(rosenbrock, init_rosen, 8, verbose=True)

print(f'\n----- Minimizando Função Quadrática')
gradient_descent_Golden_Line(t.funcaoQuadratica_args, init_quadatic, 8, verbose=True)


print('\nMinimização usando Método Explicito para funções Quadráticas\n')


gradient_descent_QD(t.funcaoQuadratica, init_quadatic, 8, verbose=True)
