import numpy as np

# Given data points
x_data = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_data = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Point to interpolate
x_interp = 4.0

# Identify the interval where x_interp lies
for i in range(len(x_data) - 1):
    if x_data[i] <= x_interp <= x_data[i + 1]:
        x1, y1 = x_data[i], y_data[i]
        x2, y2 = x_data[i + 1], y_data[i + 1]
        break

# Linear interpolation formula
y_interp = y1 + (y2 - y1) / (x2 - x1) * (x_interp - x1)

print(f"The interpolated value of y at x = {x_interp} is {y_interp:.2f}")
