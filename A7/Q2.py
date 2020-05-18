import numpy as np
import matplotlib.pyplot as plt

j = np.complex(0, 1)


def ck_analysis(sample):
    N = len(sample)
    coefficients = []
    for k in range(N):
        coefficient = 0
        for n in range(N):
            coefficient += sample[n] * np.exp(-1 * j * 2 * np.pi * k * n / N)
        coefficient /= N
        coefficients.append(np.round(coefficient, 2))
    return coefficients


def xn_synthesis(m, sample):
    N = len(sample)
    n = np.linspace(0, N - 1, N)
    coefficients = ck_analysis(sample=sample)
    xmn = []
    for n in range(N):
        value = 0
        for k in range(-m, m + 1):
            value += coefficients[k] * np.exp(j * k * 2 * np.pi * n / N)
        xmn.append(np.round(value.real, 2))
    return xmn


def draw_signals(sample, results, name):

    N = len(sample)
    n = np.arange(N)
    if name == 'v':
        fig, axs = plt.subplots(4, constrained_layout=True)
    else:
        fig, axs = plt.subplots(len(results) + 1, constrained_layout=True)

    axs[0].stem(n, sample, basefmt="k", use_line_collection=True)
    axs[0].set_title("sample")
    if name == 'v':
        axs[1].stem(n, results[0], basefmt="k", use_line_collection=True)
        axs[1].set_title("m_0")
        axs[2].stem(n, results[10], basefmt="k", use_line_collection=True)
        axs[2].set_title("m_10")
        axs[3].stem(n, results[20], basefmt="k", use_line_collection=True)
        axs[3].set_title("m_20")

    else:
        for i in range(len(results)):
            axs[i+1].stem(n, results[i], basefmt="k", use_line_collection=True)
            axs[i+1].set_title("m_{}".format(i))
    plt.savefig('Q2_{}.png'.format(name))


inputs_sample = {'ii': [1, 0.5, 0.5], 'iii': [1, 0.5, 0, 0, 0.5], 'iv': [3, 2, 1, 2],
                 'v': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]}

for sample in inputs_sample:
    results = []
    for m in range(len(inputs_sample[sample])):
        results.append(xn_synthesis(m=m, sample=inputs_sample[sample]))
    draw_signals(sample=inputs_sample[sample], results=results, name=sample)

