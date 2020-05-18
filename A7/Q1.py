import numpy as np


def ck_analysis(sample):
    N = len(sample)
    j = np.complex(0, 1)
    coefficients = []
    for k in range(N):
        coefficient = 0
        for n in range(N):
            coefficient += sample[n] * np.exp(-1 * j * 2 * np.pi * k * n / N)
        coefficient /= N
        coefficients.append(np.round(coefficient, 2))
    return coefficients


inputs_sample = {'ii': [1, 0.5, 0.5], 'iii': [1, 0.5, 0, 0, 0.5], 'iv': [3, 2, 1, 2]}
for sample in inputs_sample:
    coefficients = ck_analysis(inputs_sample[sample])
    print("coefficients for {} is: {}".format(sample, coefficients))