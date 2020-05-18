import numpy as np
import soundfile as sf
import simpleaudio as sa


def play_audio(m, p, fs, name):
    # Combine magnitude and phase parts
    f = m * np.exp(1j * p)

    # Computer inverse fft
    y = np.fft.ifft(f)
    y = np.real(y)

    # Convert to 16-bit data
    audio = y * (2 ** 15 - 1)
    audio = audio.astype(np.int16)
    sf.write(file="{}.wav".format(name), data=audio, samplerate=fs,)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()


# Read signal
signal, fs = sf.read('sound1.wav')
signal = signal[:, 0]

# Compute fft
f = np.fft.fft(signal * 2)

# Convert to polar (magnitude and phase)
m = np.abs(f)
p = np.angle(f)


# a -------------------------------------------- a
p_a = -1 * p
play_audio(m, p_a, fs, "negative_phase")

# b ------------------------------------------- b
p_b = 0
play_audio(m, p_b, fs, "zero_phase")

# c --------------------------------------------- c
# n0 = N/4
n0 = fs/4
p_c0 = p + (p * n0)
play_audio(m, p_c0, fs, "quarter_sample_rate")

# n0 = N/2
n0 = fs/2
p_c1 = p + (p * n0)
play_audio(m, p_c1, fs, "half_sample_rate")

# n0 = -N/4
n0 = -1 * (fs/4)
p_c2 = p + (p * n0)
play_audio(m, p_c2, fs, "mines_half_sample_rate")

# d ---------------------------------------------- d
m_d = 2 * m
play_audio(m_d, p, fs, "double_magnitude")

# e ----------------------------------------------- e
m_e = np.array([np.average(m)] * np.size(m))
play_audio(m_e, p, fs, "average_magnitude")


# f ------------------------------------------------ f
signal2, fs2 = sf.read('sound2.wav')
signal2 = signal2[:, 0]
min_dist = np.min([len(signal), len(signal2)])

f1 = np.fft.fft(signal[:min_dist])
m1 = np.abs(f1)
p1 = np.angle(f1)

f2 = np.fft.fft(signal2[:min_dist])
m2 = np.abs(f2)
p2 = np.angle(f2)

play_audio(m1, p2, fs, "f_out1")
play_audio(m2, p1, fs, "f_out2")