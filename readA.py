import probability 
import test
import chi

def readFile(fileName):
    import numpy as np
    import sys
    omega = []
    A = []
    try:
        ifile = open(fileName, "r")
    except:
        sys.exit(fileName + " does not exist. ")
    for index, string in enumerate(ifile):
        a = string.split()
        omega.append(float(a[0]))
        A.append(float(a[1]))
    ifile.close()
    omega = np.asarray(omega)
    A = np.asarray(A)
    return omega, A

def main():
    import sys
    import os
    import numpy as np
    import numpy.linalg
    
    G_cc_tau = []
    tau = []
    ifile = open("G_cc_tau.txt", "r")
    for index, string in enumerate(ifile):
        a = string.split()
        tau.append(float(a[0]))
        G_cc_tau.append(float(a[1]))
    ifile.close()
    beta = tau[len(tau)-1]

    tau = np.asarray(tau)
    G_cc_tau = np.asarray(G_cc_tau)
    beta = tau[len(tau)-1]
    
    ntau = len(tau)
    CM = np.zeros((ntau, ntau))
    ifile = open("CM_cc_tau.txt", "r")
    for index, string in enumerate(ifile):
        a = string.split()
        row = int(a[0])
        col = int(a[1])
        CM[row-1, col-1] = float(a[2])
    ifile.close()
    for i in range(ntau):
        CM[i, i] = 0.01**2
    C_inv = numpy.linalg.inv(CM)

    alpha = []
    ifile = open("alpha.txt", "r")
    for index, string in enumerate(ifile):
        alpha.append(float(string.strip()))
    ifile.close()

    P = []
    spectrals = []
    chi_values = []
    for i in range(len(alpha)):
        print alpha[i]
        omega, A = readFile("A_updated_alpha_" + str(alpha[i]) + ".txt")
        P.append(probability.probability(alpha[i], G_cc_tau, A, tau, omega, beta, C_inv))
        spectrals.append(A)
        chi_values.append(chi.chi(G_cc_tau, A, tau, omega, beta, C_inv))

    Nomega = len(omega)
    spectral_mean = np.zeros(Nomega)
    for i in range(1, len(alpha)):
        spectral_mean = spectral_mean + (-alpha[i] + alpha[i-1])*P[i]*spectrals[i]

    s = 0.0
    for i in range(1, len(P)):
        s = s + P[i]*(-alpha[i]+alpha[i-1])
    spectral_mean = spectral_mean/s
    test.printFile(omega, spectral_mean, "bryan.txt")
    test.printFile(alpha, chi_values, "Chi_alpha.txt")
    ofile = open("P_log_alpha.txt", "w")
    for i in range(len(alpha)):
        ofile.write(str(np.log(alpha[i])) + "    " + str(P[i]) + "\n")
    ofile.close()
    return 0

main()

