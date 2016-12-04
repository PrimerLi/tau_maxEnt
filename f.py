import default
import kernel

def f(alpha, G, A, tau, omega, beta, C_inv):
    import numpy as np

    domega = omega[1] - omega[0]
    Nomega = len(omega)
    result = np.zeros(Nomega)
    for nw in range(Nomega):
        result[nw] = -alpha*domega*(1 + np.log(A[nw]/default.D(omega[nw]))) 

    ntau = len(tau)
    vector_right = G - kernel.KMatrix(tau, beta, omega).dot(A)
    result = result + np.transpose(kernel.KMatrix(tau, beta, omega)).dot(C_inv).dot(vector_right)
    return result
