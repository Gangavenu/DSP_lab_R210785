import numpy as np
import matplotlib.pyplot as plt
fs = 3000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time array
t=np.arange(0,3000)
x = np.sin(2 * np.pi * 10 * t/fs)  # Sinusoidal signal
X = np.fft.fft(x)
# Find the peak
peak_index = np.argmax(np.abs(X))
peak_value = np.abs(X[peak_index])
# Calculate k
k = peak_index / len(X) * fs
# Verify the peak
print("Peak value:", peak_value)
print("k:", k)
# Plot the signal and its DFT
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Sinusoidal Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.plot(np.abs(X))
plt.title("DFT of Sinusoidal Signal")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
