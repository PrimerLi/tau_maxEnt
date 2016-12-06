def readA(fileName):
    omega = []
    A = []
    ifile = open(fileName, "r")
    for i, string in enumerate(ifile):
        a = string.split()
        omega.append(float(a[0]))
        A.append(float(a[1]))
    ifile.close()
    return omega, A

def K(tau, omega, beta):
    import numpy as np
    return -np.exp(-tau*omega)/(1 + np.exp(-beta*omega))

def printFile(x, y, output):
    ofile = open(output, "w")
    for i in range(len(x)):
        ofile.write(str(x[i]) + "    " + str(y[i]) + "\n")
    ofile.close()

def main():
    import os
    import sys

    if (len(sys.argv) != 3):
        print "beta = sys.argv[1], fileName = sys.argv[2]. "
        return -1 

    beta = float(sys.argv[1])
    fileName = sys.argv[2]

    omega, A = readA(fileName)
    domega = omega[1] - omega[0]
    tau = []
    dtau = 0.1
    ntau = int(beta/dtau) + 1
    for i in range(ntau):
        tau.append(i*dtau)
    G = []
    for i in range(len(tau)):
        KA = 0
        for nw in range(len(omega)):
            KA = KA + domega*K(tau[i], omega[nw], beta)*A[nw]
        G.append(KA)

    printFile(tau, G, "G_tau.txt")
    return 0

main()
