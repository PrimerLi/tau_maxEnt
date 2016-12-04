import default
import f
import J

def norm(vector):
    import numpy as np
    s = 0.0
    for i in range(len(vector)):
        s = s + vector[i]**2
    return np.sqrt(s)

def Newton(alpha, G, A_initial, tau, omega, beta, C_inv):
    import numpy as np
    import numpy.linalg

    Nomega = len(A_initial)
    A_updated = np.zeros(Nomega)
    iterationMax = 100
    eps = 0.0001
    counter = 0
    while (True):
        counter = counter + 1
        if (counter > iterationMax):
            break
        J_inv = numpy.linalg.inv(J.J(alpha, G, A_initial, tau, omega, beta, C_inv))
        A_updated = A_initial - J_inv.dot(f.f(alpha, G, A_initial, tau, omega, beta, C_inv))
        diff = norm(A_updated - A_initial)
        print counter, diff
        if (diff < eps):
            break
        A_initial = A_updated
    return A_initial
