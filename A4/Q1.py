import numpy as np
import matplotlib.pyplot as plt


def u(n):
    return np.heaviside(n, 1)


rngx = 50
pi = np.degrees(np.pi)
n = np.linspace(-rngx, rngx, 2 * rngx + 1)
hn = u(n - 1) - u(n - 14)

# a
xn_a = u(n - 1) - (2*u(n - 4)) + u(n - 7)
yn_a = np.convolve(xn_a, hn, mode="same")
fig, axs = plt.subplots(2)
axs[0].stem(n, xn_a, '-', use_line_collection=True)
axs[0].set_title("input")
axs[1].stem(n, yn_a, '-', use_line_collection=True)
axs[1].set_title("output")
plt.savefig("Q1a.png")
plt.show()

# b
xn_b = (u(n) - u(n - 12)) * np.sin(np.radians(pi/6) * n)
yn_b = np.convolve(xn_b, hn, mode="same")
fig, axs = plt.subplots(2)
axs[0].stem(n, xn_b, '-', use_line_collection=True)
axs[0].set_title("input")
axs[1].stem(n, yn_b, '-', use_line_collection=True)
axs[1].set_title("output")
plt.savefig("Q1b.png")
plt.show()