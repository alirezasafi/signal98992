import numpy as np
from scipy.signal import lfilter
import soundfile

in_fname = "q4_input.wav"
data, samplerate = soundfile.read(file=in_fname)
xn = data[:, 0]
N = int(samplerate / 2)
b = [1]


#  a = 0.5
a1 = np.concatenate([[1], np.zeros(N - 1), [-0.5]])
yn1 = lfilter(b=b, a=a1, x=xn)
out_fname1 = "q4_output1.wav"
soundfile.write(file=out_fname1, data=yn1, samplerate=samplerate)

# a = -0.5
a2 = np.concatenate([[1], np.zeros(N - 1), [0.5]])
yn2 = lfilter(b=b, a=a2, x=xn)
out_fname2 = "q4_output2.wav"
soundfile.write(file=out_fname2, data=yn2, samplerate=samplerate)
