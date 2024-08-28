import numpy as np

# Function to calculate DFT
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X
# Function to calculate IDFT
def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x.real

# Function to perform circular convolution
def circular_convolution(x, h):
    N = len(h)
    x_padded = np.pad(x, (0, N - len(x)))  # Pad x with zeros
    X = dft(x_padded)
    H = dft(h)
    Y = X * H
    y = idft(Y)
    return y

# Define two sequences
x = np.array([4, 3, 2, 1])
h = np.array([1, -2, 0, 4])

# Perform circular convolution
y = circular_convolution(x, h)

# Print result
print("Circular Convolution:", y)


