import kernel

def gauss(omega, mu, sigma):
    import numpy as np
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(omega - mu)**2/(2*sigma**2))

def lorentz(omega, mu, gamma):
    import numpy as np
    return 1/(np.pi*gamma)*1/(1 + ((omega - mu)/gamma)**2)

def spectral(omega):
    return 0.5*gauss(omega, -1.2, 0.3) + 0.5*gauss(omega, 1.2, 0.4)

def getSpectral():
    import numpy as np
    Nomega = 100
    omega_lower = -5
    omega_upper = -omega_lower
    domega = (omega_upper - omega_lower)/float(Nomega-1)
    omega = np.zeros(Nomega)
    for nw in range(Nomega):
        omega[nw] = omega_lower + nw*domega
    A = np.zeros(Nomega)
    for nw in range(Nomega):
        #A[nw] = lorentz(omega[nw], mu, gamma)
        A[nw] = spectral(omega[nw])
    return omega, A    

def printFile(x, y, fileName):
    ofile = open(fileName, "w")
    for i in range(len(x)):
        ofile.write(str(x[i]) + "    " + str(y[i]) + "\n")
    ofile.close()

def main():
    import os
    import sys
    import numpy as np
    import random

    mu = 0.0
    gamma = 0.6
    omega, spectral_values = getSpectral()
    printFile(omega, spectral_values, "spectral.txt")

    beta = 10
    dtau = 0.1
    ntau = int(beta/dtau)+1
    tau = np.zeros(ntau)
    for i in range(ntau):
        tau[i] = i*dtau

    Gtau = kernel.KMatrix(tau, beta, omega).dot(spectral_values)

    error = 0.001
    for i in range(ntau):
        Gtau[i] = Gtau[i] + random.gauss(0, error)

    printFile(tau, Gtau, "G_cc_tau.txt")

    CM = np.zeros((ntau, ntau))
    for i in range(ntau):
        CM[i,i] = error**2
        
    ofile = open("CM_cc_tau.txt", "w")
    for i in range(ntau):
        for j in range(ntau):
            ofile.write(str(i) + "    " + str(j) + "    " + str(CM[i,j]) + "\n")
    ofile.close()
    return 0

main()
