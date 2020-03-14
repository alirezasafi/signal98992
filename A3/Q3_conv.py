import numpy as np


def convolution(x_seq, h_seq):
    k_start = -len(h_seq) + 1
    k_end = len(h_seq) + len(x_seq) - 1
    k_length = k_end - k_start + 1
    x_length = len(x_seq)
    h_length = len(h_seq)

    for i in range(0, -k_start):
        x_seq.insert(0,0)

    for i in range(0, k_length - len(x_seq)):
        x_seq.append(0)

    h_seq.reverse()

    for i in range(0, k_length - h_length):
        h_seq.append(0)

    result = np.zeros(x_length + h_length - 1)
    index = 0
    while index < len(result):
        for i in range(0, k_length):
            result[index] += x_seq[i] * h_seq[i]
        index += 1
        h_seq = list(np.roll(h_seq, 1))  # shift left h sequence.
    return result
