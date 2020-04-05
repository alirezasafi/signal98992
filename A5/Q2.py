import numpy as np
import soundfile


def u(n):
    return np.heaviside(n, 1)


def add_noise_sys(in_fname):
    in_data, samplerate = soundfile.read(in_fname)
    out_data = in_data + np.random.randn(in_data.shape[0]) * 0.025
    out_fname = "q2_noise_signal.wav"
    soundfile.write(file=out_fname, samplerate=samplerate, data=out_data)
    return samplerate, out_data


def average_sys(m, in_data, samplerate):
    xn = in_data
    rngx = len(xn) // 2
    n = np.linspace(-rngx, rngx, 2 * rngx + 1)
    hn = (u(n) - u(n - m)) / m
    yn = np.convolve(xn, hn, mode="same")
    out_fname= "q2_average_{}.wav".format(str(m))
    soundfile.write(file=out_fname, data=yn, samplerate=samplerate)


samplerate, average_input = add_noise_sys(in_fname="signal.wav")
average_sys(m=20, in_data=average_input*100, samplerate=samplerate)
average_sys(m=100, in_data=average_input*100, samplerate=samplerate)
average_sys(m=2000, in_data=average_input*100, samplerate=samplerate)

