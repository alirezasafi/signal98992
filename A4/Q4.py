import numpy as np
from scipy.io import wavfile


def u(n):
    return np.heaviside(n, 1)


def delta(n):
    return u(n) - u(n - 1)


in_fname = "input.wav"
samplerate, data = wavfile.read(in_fname)

xn = data[:, 0]  # left channel.
N = int(samplerate / 2)
rngx = len(xn)//2
n = np.linspace(-rngx, rngx, 2 * rngx + 1)
hn = delta(n) + ((delta(n - N)) / 2) + ((delta(n - (2 * N))) / 4) + ((delta(n - (3 * N))) / 8)
yn = np.convolve(xn, hn)

out_fname = "output.wav"
wavfile.write(filename=out_fname, rate=samplerate, data=yn)
