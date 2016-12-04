import kernel

def chi(G, A, tau, omega, beta, C_inv):
    import numpy as np
    ntau = len(tau)
    vector = G - kernel.KMatrix(tau, beta, omega).dot(A) 
    return np.transpose(vector).dot(C_inv).dot(vector)
