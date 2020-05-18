import numpy as np
import matplotlib.pyplot as plt


n = np.arange(61)
length_n = len(n)
N = 8
j = np.complex(0, 1)
pi = np.pi
xn = [1, 2, 3, 4, 3, 2, 1, 0] * ((length_n // N) + 1)
xn = xn[:length_n]

# a
hn1 = [2, -1, 1, 3, 6, 3, 1, -1, 2]
yn1 = np.convolve(xn, hn1, mode='same')

fig1, axs1 = plt.subplots(2, constrained_layout=True)
axs1[0].stem(n, xn, use_line_collection=True)
axs1[0].set_title("xn")
axs1[1].stem(n, yn1, use_line_collection=True)
axs1[1].set_title("yn1")
fig1.savefig("Q4_a.png")

# b
H2 = np.ones(length_n) * (5 * np.exp(j * (pi / 4)))
X2 = (1 / N) * np.fft.fft(xn)
Y2 = H2 * X2
yn2 = N * np.fft.ifft(Y2)

fig2, axs2 = plt.subplots(2, constrained_layout=True)
axs2[0].stem(n, xn, use_line_collection=True)
axs2[0].set_title("xn")
axs2[1].stem(n, yn2, use_line_collection=True)
axs2[1].set_title("yn2")
fig2.savefig("Q4_b.png")

# c
hn3 = [1, 0.5, 0.25, 0.125, 0.0625]
yn3 = np.convolve(xn, hn3, mode='same')

fig3, axs3 = plt.subplots(2, constrained_layout=True)
axs3[0].stem(n, xn, use_line_collection=True)
axs3[0].set_title("xn")
axs3[1].stem(n, yn3, use_line_collection=True)
axs3[1].set_title("yn3")
fig3.savefig("Q4_c.png")
