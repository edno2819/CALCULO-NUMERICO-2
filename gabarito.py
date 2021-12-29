from scipy.optimize import minimize
import Functions 


t = Functions.Quadatic_explicit()
init_himmme =  [2, 5]
init_rosen = [-1.2, 1]
init_quadatic = [2,2,5]

solutionHimme = minimize(Functions.himmelblau, init_himmme)
solutionRosen = minimize(Functions.rosenbrock, init_rosen)
solutionQP = minimize(t.funcaoQuadratica, init_quadatic)

print('Gabarito:\nMinimo das soluções das funções problemas')
print('Função Himmelblau')
print(f'{solutionHimme.x} : {Functions.himmelblau(solutionHimme.x)}')
print('Função Rosenbrock')
print(f'{solutionRosen.x} : {Functions.rosenbrock(solutionRosen.x)}')
print('Função Quadrática')
print(f'{solutionQP.x} : {t.funcaoQuadratica(solutionQP.x)}')
