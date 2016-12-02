import kernel

def chi(G, A, tau, omega, beta, C_inv):
    import numpy as np
    ntau = len(tau)
    vector = np.zeros(ntau)
    for nt in range(ntau):
        KA = kernel.KMatrix(tau, beta, omega).dot(A)
        vector[nt] = G[nt] - KA
    return np.transpose(vector).dot(C_inv).dot(vector)
