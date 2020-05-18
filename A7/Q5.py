import numpy as np
import matplotlib.pyplot as plt
from A7.Q1 import ck_analysis

# a
xn = []
for i in range(0, 11):
    if 0 <= i <= 5:
        xn.append(i)
    elif 5 < i < 10:
        xn.append(10 - i)
    else:
        xn.append(0)

dtft_xn = np.fft.fft(xn, n=10000)
print("DTFT xn is: ", np.round(dtft_xn, 2))

nforxn = np.arange(len(xn))
fig, axs = plt.subplots(3, constrained_layout=True)
axs[0].stem(nforxn, xn, use_line_collection=True)
axs[0].set_title("xn")
axs[1].stem(nforxn, np.abs(xn), use_line_collection=True)
axs[1].set_title("abs(xn)")
axs[2].stem(nforxn, np.angle(xn), use_line_collection=True)
axs[2].set_title("angle(xn)")
plt.savefig('Q5_a.png')


# b

input_sample = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
N = len(input_sample)
fig, axs = plt.subplots(4, constrained_layout=True)

# dtfs with fft
dtfs1_xn = np.fft.fft(input_sample) / N
dtfs1_xn = np.round(dtfs1_xn, 2)
print("Q5-b with fft: ", dtfs1_xn)
axs[0].stem(np.arange(len(dtfs1_xn)), np.real(dtfs1_xn), use_line_collection=True)
axs[0].set_title("dtfs with fft real")
axs[1].stem(np.arange(len(dtfs1_xn)), np.imag(dtfs1_xn), use_line_collection=True)
axs[1].set_title("dtfs with fft imaginary")

# dtfs with Q1
dtfs2_xn = ck_analysis(input_sample)
print("Q5-b with Q1:", dtfs1_xn)
axs[2].stem(np.arange(len(dtfs2_xn)), np.real(dtfs2_xn), use_line_collection=True)
axs[2].set_title("dtfs with Q1 real")
axs[3].stem(np.arange(len(dtfs2_xn)), np.imag(dtfs2_xn), use_line_collection=True)
axs[3].set_title("dtfs with Q1 imaginary")
plt.savefig('Q5_b.png')
