import numpy as np 
import copy
from Functions import himmelblau
import math


def Golden_Line(func_var,  x, search, a=-100, b=100,   maxiter=100, epsilon=0.0002):
        tau = 0.381967
        alpha1 = a*(1-tau) + b* tau
        alpha2 = a* tau + b*(1-tau)
        falpha1 = func_var(x+alpha1 * search)
        falpha2 = func_var(x+alpha2 * search)
        for k in range(1,maxiter):

                if (falpha1 > falpha2):
                        a = alpha1
                        alpha1 = alpha2
                        falpha1 = falpha2
                        alpha2 = tau*a + (1-tau)*b
                        falpha2 = func_var(x+alpha2 * search)

                else:
                        b = alpha2
                        alpha2 = alpha1
                        falpha2 = falpha1
                        alpha1 = tau*b + (1-tau)*a
                        falpha1 = func_var(x+alpha1 * search)

                if (abs(func_var(x+alpha1 * search) - func_var(x+alpha2 * search))< epsilon):
                        break


        golden = (alpha1 , falpha1)
        return (golden)


def norm(vetor, ord):
        ord = int(ord)
        return sum(abs(vetor)**ord)**(1./ord)


def Grad_Vec(func_var, x):
        '''teste Grad_Vec
                def func_var(x):
                return x[2]*math.exp(x[0]+x[1])+x[2]**2
                Grad_Vec(func_var, [1, 1, 2])
                [14.778114660877861, 14.778114660877861, 11.389056098929373]'''
                
        delx = 0.001
        Grad_Vec = []
        for i in range(0,len(x)):
                xvec = copy.deepcopy(x)
                xvec1 = copy.deepcopy(x)
                xvec[i] = x[i] + delx
                xvec1[i] = x[i] - delx
                Grad_Vec.append((func_var(xvec) - func_var(xvec1) )/(2*delx))
        return np.array(Grad_Vec)


def gradient_descent_with_Golden_Line(func_var, x, epsilon , maxiter, learning_rate):
        func_previous = func_var(x)
        print(f'Initial function value: {round(func_previous, 4)}\n\n')
        print('k x f(x) ||gradient||','\n')
        for iter in range(0,maxiter):
                gradient = Grad_Vec(func_var, x) 
                search_direction = -1*gradient 
                alpha, func_alpha  = learning_rate(func_var, x, search_direction, epsilon=epsilon ,maxiter=maxiter)
                func_previous =  func_alpha
                x = x + alpha * search_direction
                if abs(func_previous) <= epsilon:
                        break

        print(f'Iteração N {iter}')
        print(f"\nMinimum point: {x}")
        print(f"\nMinimum function value: {func_previous}")
        return (x)


# a = 1
# b = 5
# x = np.array([2,5])

# gradient_descent_with_Golden_Line(himmelblau, x, 0.001, 102, learning_rate=Golden_Line)


def Fibonacci_Search(func_var, a, b, n):
        print('k a b f(x1) f(x2) \n')
        N=n+1
        fold=1
        fnew=1
        f = []
        #Generate seqience of Fibonacci numbers
        for i in range(0,N):
                if i==1 or i==2:
                        f.append(1)
                        next
                f.append(fold+fnew)
                fold=fnew
                fnew =f[i]

        L2=(b-a)*f[N-2]/f[N]
        x1=a+L2
        x2=b-L2
        fx1=func_var(x1)
        fx2=func_var(x2)
        j=0

        for j in range(1,N):
                L0=(b-a)
                #The comparison is made to ensure x1 lies to the left of x2
                if L2>L0/2:
                        anew=b-L2
                        bnew=a+L2
                else:
                        if (L2 <=L0/2):
                                anew=a+L2
                                bnew=b-L2
                fx1=func_var(anew)
                fx2=func_var(bnew)
                #calculo do novo intervalo
                if fx2>fx1:
                        b=bnew
                        L2=f[N-j]*L0/f[N-j+2]
                else:
                        if fx2<fx1:
                                a=anew
                                L2=f[N-j]*L0/f[N-(j-2)]
                        else:
                                if fx2==fx1:
                                        b=bnew
        L2=f[N-j]*(b-a)/f[N-(j-2)]

        print(j-1, a, b,fx1, fx2)
        print(f'\nMinimum point:{a}')
        print(f'\nMinimum function value:{func_var(a)}')


def F(n):
        if n == 0: return 1
        elif n == 1: return 1
        else: return F(n-1)+F(n-2)

def calcule_fibo(func_var, iter, a, b, n, L0):
        L_G = ((F(n-iter))/F(n))*L0
        x1 = a + L_G
        x2 = b - L_G
        if func_var(x1) < func_var(x2):
                return a, x2
        else:
                return 

def func_var(x):
        fx=x+math.exp(math.sin(x))
        return(fx)

pi = 3.14
a = -pi/2
b = pi/2
n = 16
Fibonacci_Search(func_var, a, b, n)