import kernel 
import default

def J(alpha, G, A, tau, omega, beta, C_inv):
    import numpy as np
    import sys

    ntau = len(tau)
    domega = omega[1] - omega[0]
    
    result = -np.transpose(kernel.KMatrix(tau, beta, omega)).dot(C_inv).dot(kernel.KMatrix(tau, beta, omega))
    shape = result.shape
    if (shape[0] != shape[1]):
        sys.exit("J matrix should be square. ")
    dimension = shape[0]
    if (dimension != len(omega)):
        print "Dimension of J is ", dimension, ", dimension of omega is ", len(omega)
        sys.exit("J matrix should have the same dimension as the length of omega. ")
    for i in range(dimension):
        result[i, i] = result[i,i] - alpha*domega/A[i]
    return result
