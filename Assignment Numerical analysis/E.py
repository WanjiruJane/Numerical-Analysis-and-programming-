import numpy as np
import matplotlib.pyplot as plt

def compute_fft():
    # Parameters
    f1 = 50  # Frequency of the first sine wave
    f2 = 120  # Frequency of the second sine wave
    sample_rate = 1000  # Sampling rate in Hz
    duration = 1  # Duration of the signal in seconds

    # Time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Signal
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Compute FFT
    fft_result = np.fft.fft(s)
    fft_freq = np.fft.fftfreq(len(fft_result), 1/sample_rate)

    # Plot the original signal
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, s)
    plt.title("Original Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Plot the FFT result
    plt.subplot(2, 1, 2)
    plt.stem(fft_freq, np.abs(fft_result), 'b', markerfmt=" ", basefmt="-b")
    plt.title("FFT of the Signal")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 200)  # Limit x-axis to show the relevant frequencies

    plt.tight_layout()
    plt.show()

# Call the function to compute FFT and plot the results
compute_fft()
