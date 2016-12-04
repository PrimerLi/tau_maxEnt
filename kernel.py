def K(tau, beta, omega):
    import numpy as np
    return -np.exp(-tau*omega)/(1 + np.exp(-beta*omega))

def KMatrix(tau, beta, omega):
    import numpy as np
    ntau = len(tau)
    Nomega = len(omega)
    matrix = np.zeros((ntau, Nomega))
    domega = omega[1] - omega[0]
    for nt in range(ntau):
        for nw in range(Nomega):
            matrix[nt, nw] = K(tau[nt], beta, omega[nw])*domega/(2*np.pi)
    return matrix
