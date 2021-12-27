import numpy as np
import quadprog
import scipy
import scipy.linalg

def quadprog_solve_qp(P, q, G=None, h=None, A=None, b=None, initvals=None):
    if initvals is not None:
        print("quadprog: note that warm-start values ignored by wrapper")
    qp_G = P
    qp_a = -q
    if A is not None:
        qp_C = -vstack([A, G]).T
        qp_b = -hstack([b, h])
        meq = A.shape[0] if A.ndim > 1 else 1
    else:  # no equality constraint
        qp_C = -G.T
        qp_b = -h
        meq = 0
    return solve_qp(qp_G, qp_a, qp_C, qp_b, meq)[0]


def quadprog_solve_qp(P, q, G=None, h=None, A=None, b=None):
    qp_G = .5 * (P + P.T)
    qp_a = -q
    if A is not None:
        qp_C = -np.vstack([A, G]).T
        qp_b = -np.hstack([b, h])
        meq = A.shape[0]
    else:  # no equality constraint
        qp_C = -G.T
        qp_b = -h
        meq = 0
    return quadprog.solve_qp(qp_G, qp_a, qp_C, qp_b, meq)[0]


def verify(G, a, C=None, b=None):
    xf0, f0 = quadprog.solve_qp(G, a, C, b)[0:2]
    xf1, f1 = quadprog.solve_qp(scipy.linalg.inv(scipy.linalg.cholesky(G)), a, C, b, factorized=True)[0:2]

    np.testing.assert_array_almost_equal(xf0, xf1)
    np.testing.assert_almost_equal(f0, f1)


def test_1():
    G = np.eye(3, 3)
    a = np.array([0, 5, 0], dtype=np.double)
    C = np.array([[-4, 2, 0], [-3, 1, -2], [0, 0, 1]], dtype=np.double)
    b = np.array([-8, 2, 0], dtype=np.double)
    xf, f, xu, iters, lagr, iact = quadprog.solve_qp(G, a, C, b)
    np.testing.assert_array_almost_equal(xf, [0.4761905, 1.0476190, 2.0952381])
    np.testing.assert_almost_equal(f, -2.380952380952381)
    np.testing.assert_almost_equal(xu, [0, 5, 0])
    np.testing.assert_array_equal(iters, [3, 0])
    np.testing.assert_array_almost_equal(lagr, [0.0000000, 0.2380952, 2.0952381])

    verify(G, a, C, b)

test_1()