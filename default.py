def gauss(omega, mu, sigma):
    import numpy as np
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(omega - mu)**2/(2*sigma**2))

def D(omega):
    mu = 0
    sigma = 1.0
    return gauss(omega, mu, sigma)
