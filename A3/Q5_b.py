import numpy as np
import matplotlib.pyplot as plt

x = np.cos(np.linspace(0, 4. * np.pi, 100))
y1 = np.convolve(np.ones(5), x)
y2 = np.convolve([1, -1, -1, -1, 1], x)
y = np.convolve(np.ones(3), y1 + y2)

h = [2, 2, 2, 0, 2, 2, 2]  # np.convolve(np.ones(3),np.ones(5)+[1,-1,-1,-1,1])
y_prim = np.convolve(h, x)
n = np.arange(-53, 53, 1)

fig, signals = plt.subplots(2)
signals[0].stem(n, y, '-', use_line_collection=True)
signals[0].set_title("y = [1,1,1] * (y1 + y2)")

signals[1].stem(n, y_prim, '-', use_line_collection=True)
signals[1].set_title("y = convolve(h, x)")
plt.savefig("Q5_b.png")
