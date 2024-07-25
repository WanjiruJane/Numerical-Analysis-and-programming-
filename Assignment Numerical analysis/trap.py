import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return np.sin(x)

# Implement the trapezoidal rule
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    area = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return area

# Parameters
a = 0  # Start point
b = np.pi  # End point
n = 10  # Number of trapezoids

# Compute the area using the trapezoidal rule
area = trapezoidal_rule(f, a, b, n)
print(f"Approximate area under sin(x) from {a} to {b} using {n} trapezoids: {area}")

# Visualization
x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y, label='f(x) = sin(x)', color='blue')

# Plot the trapezoids
x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)
for i in range(n):
    plt.fill([x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]],
             [0, y_trap[i], y_trap[i+1], 0], 'b', edgecolor='r', alpha=0.2)

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoidal Rule for Numerical Integration')
plt.show()
