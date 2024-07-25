import numpy as np
import matplotlib.pyplot as plt

# Define a function
def f(x):
    return x**2 + 2*x + 1

# Generate some data points
x = np.linspace(-10, 10, 100)
y = f(x)

# Compute the gradient (numerical derivative)
dy_dx = np.gradient(y, x)

# Plot the function and its derivative
plt.plot(x, y, label='f(x)')
plt.plot(x, dy_dx, label="f'(x)", linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Function and its Derivative')
plt.show()
