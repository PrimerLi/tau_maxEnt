import entropy
import chi

def Q(alpha, G, A, tau, omega, beta, C_inv):
    return alpha*entropy.entropy(omega, A) - 0.5*chi.chi(G, A, tau, omega, beta, C_inv)
