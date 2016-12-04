import Q

def probability(alpha, G, A, tau, omega, beta, C_inv):
    import numpy as np
    return np.exp(Q.Q(alpha, G, A, tau, omega, beta, C_inv))
