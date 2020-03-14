import numpy as np
import matplotlib.pyplot as plt
from A3.Q3_conv import convolution

# b) x[n] = u[n] - u[n-3] , h[n] = u[n] - u[n-2]

n = np.linspace(-50, 50, 101)

fig, signals = plt.subplots(3)
x_seq = np.heaviside(n, 1) - np.heaviside(n-3, 1)
signals[0].stem(n, x_seq, '-', use_line_collection=True)
signals[0].set_title('x[n] = u[n] - u[n-3]')

h_seq = np.heaviside(n, 1) - np.heaviside(n-2, 1)
signals[1].stem(n, h_seq, '-', use_line_collection=True)
signals[1].set_title('h[n] = u[n] - u[n-2]')

conv_seq = convolution(list(x_seq), list(h_seq))
# conv_seq = np.convolve(x_seq, h_seq)
n = np.linspace(-100, 100, 201)
signals[2].stem(n, conv_seq, '-', use_line_collection=True)
signals[2].set_title('convolve(x[n], h[n])')
plt.savefig("Q3_b.png")
