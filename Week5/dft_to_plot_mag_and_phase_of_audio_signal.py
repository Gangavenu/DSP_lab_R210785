import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

# Load audio WAV file
fs, audio = wavfile.read('/home/r210785/Documents/CL_LAB/week-7/Chorus.wav')

# Perform DFT
dft = np.fft.fft(audio)

# Calculate magnitude and phase spectra
magnitude = np.abs(dft)
phase = np.angle(dft)

# Plot spectra
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(magnitude)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(phase)
plt.title('Phase Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()
