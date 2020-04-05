import numpy as np
import matplotlib.pyplot as plt

T0 = 6
t = np.linspace(-T0 / 2, T0 / 2, 1000)


def ck(k):
    j = np.complex(0, 1)
    if k != 0:
        return np.cos(((2 * np.pi) / 3) * k) / (j * k * np.pi) - np.cos((np.pi / 3) * k) / (j * k * np.pi)
    return 0


def xt(m=0):
    j = np.complex(0, 1)
    sigma = 0
    for k in range(-m, m + 1):
        sigma += ck(k=k) * np.exp(j * k * 2 * np.pi * t / T0)
    return sigma.real


fig, axs = plt.subplots(5)
m_lits = [1, 2, 5, 10, 50]

for i in range(len(m_lits)):
    xm = xt(m=m_lits[i])
    axs[i].plot(t, xm)
fig.suptitle('M=1, M=2, M=5, M=10, M=50')
plt.savefig("Q2.png")