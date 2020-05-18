import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
n = np.linspace(-200, 200, 401)

nd = 0
hn = ((-1 * np.sin((7 * pi) / 8 * (n - nd)) / 3) + (-1 * np.sin(pi * (n - nd)) / 3) + (
        -2 * np.sin((3 * pi) / 8 * (n - nd)) / 3) + (2 * np.sin((5 * pi) / 8 * (n - nd)) / 3) + (
                  np.sin(pi / 8 * (n - nd)))) / (pi * (n - nd))

plt.stem(n, hn, use_line_collection=True)
plt.savefig("Q3.png")
