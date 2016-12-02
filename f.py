import default
import kernel

def f(alpha, G, A, tau, omega, beta, C_inv):
    import numpy as np

    Nomega = len(omega)
    result = np.zeros(Nomega)
    result[:] = - alpha*(1 + np.log(A[:])/default.D(omega[:])) 

    ntau = len(tau)
    vector_right = np.zeros(ntau)
    
    vector_right = G - kernel.KMatrix(tau, beta, omega).dot(A)
    result = result + np.transpose(kernel.KMatrix(tau, beta, omega)).dot(C_inv).vector_right
    return result
