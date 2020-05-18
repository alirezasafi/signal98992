import numpy as np
import matplotlib.pyplot as plt

j = np.complex(0, 1)
pi = np.pi
w = np.linspace(-1, 1, 1000)
# calculate b
b = np.min(np.abs((1 - (0.8 * np.exp(-1 * j * w * pi)) + (0.81 * np.exp(-2 * j * w * pi)))))
print(b)
H = b / (1 - (0.8 * np.exp(-1 * j * w * pi)) + (0.81 * np.exp(-2 * j * w * pi)))

H_mag = np.abs(H)

plt.plot(w, H_mag)
plt.savefig("Q1.png")
