import probability
import chi
import Q
import Newton
import probability
import printFile

def gauss(x, mu, sigma):
    import numpy as np
    return 1.0/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2.0*sigma**2))

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

    tau = np.asarray(tau)
    G_cc_tau = np.asarray(G_cc_tau)

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
        CM[i, i] = 0.007**2
    C_inv = numpy.linalg.inv(CM)

    if (os.path.exists("A_initial.txt")):
        omega = []
        A_initial = []
        ifile = open("A_initial.txt", "r")
        for index, string in enumerate(ifile):
            a = string.split()
            omega.append(float(a[0]))
            A_initial.append(float(a[1]))
        ifile.close()
        omega = np.asarray(omega)
        A_initial = np.asarray(A_initial)
    else:
        Nomega = 100
        lower = -5
        upper = -lower
        domega = (upper - lower)/float(Nomega-1)
        omega = np.zeros(Nomega)
        A_initial = np.zeros(Nomega)
        for nw in range(Nomega):
            omega[nw] = lower + nw*domega
            A_initial[nw] = gauss(omega[nw], 0, 1)
        printFile.printFile(omega, A_initial, "A_initial.txt")

    Nomega = len(omega)
    beta = tau[len(tau)-1]

    Nalpha = 30
    alpha = np.zeros(Nalpha)
    for i in range(len(alpha)):
        alpha[i] = 0.02*np.exp(-i*0.07)
    ofile = open("alpha.txt", "a")
    for i in range(len(alpha)):
        ofile.write(str(alpha[i]) + "\n")
    ofile.close()

    for i in range(len(alpha)):
        print "alpha = ", alpha[i], " , i = ", i+1
        A_updated = Newton.Newton(alpha[i], G_cc_tau, A_initial, tau, omega, beta, C_inv)
        A_initial = A_updated
        output = "A_updated_alpha_" + str(alpha[i]) + ".txt" 
        printFile.printFile(omega, A_updated, output)
        os.system("cp " + output + " A_initial.txt")

    return 0

main()
