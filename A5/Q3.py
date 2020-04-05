import numpy as np
from scipy.signal import lfilter


def u(n):
    return np.heaviside(n, 1)


def delta(n):
    return u(n) - u(n - 1)


n = np.linspace(-4, 19, 24)
N = 44100
xn1 = u(n)
xn2 = delta(n)


b = [1, 0.8, 0.64]
a = [1]
yn1 = lfilter(b=b, a=a, x=xn1)
print("Step response:", yn1)
yn2 = lfilter(b=b, a=a, x=xn2)
print("Impulse response:", yn2)

