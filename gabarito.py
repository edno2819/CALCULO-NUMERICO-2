from scipy.optimize import minimize
import Functions 



init_himmme =  [2, 5]
init_rosen = [-1.2, 1]
init_qp = [2,2,5, 1,2,3,0,6,3]

Functions.quadratica_QP(init_qp)
solutionHimme = minimize(Functions.himmelblau, init_himmme, method='SLSQP')
solutionRosen = minimize(Functions.rosenbrock, init_rosen, method='SLSQP')
#solutionQP = minimize(Functions.quadratica_QP, init_qp, method='SLSQP')

print('Gabarito:\nMinimo das soluções das funções problemas')
print('Função Himmelblau')
print(f'{solutionHimme.x} - {Functions.himmelblau(solutionHimme.x)}')
print('Função Rosenbrock')
print(solutionRosen.x)
