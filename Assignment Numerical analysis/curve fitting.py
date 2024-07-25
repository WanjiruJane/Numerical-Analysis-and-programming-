import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Generate the data
# True parameters
a_true = 2.5
b_true = 1.3
c_true = 0.5

# Generate x values
x_data = np.linspace(-10, 10, 100)

# Generate y values with some noise
np.random.seed(42)  # For reproducibility
y_data = a_true * x_data**2 + b_true * x_data + c_true + np.random.normal(0, 5, size=x_data.shape)

# Step 2: Define the model function
def quadratic_model(x, a, b, c):
    return a * x * x + b * x + c

# Step 3: Fit the curve
initial_guess = [1, 1, 1]  # Initial guess for the parameters
params, covariance = curve_fit(quadratic_model, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, b_fit, c_fit = params

print(f"Fitted parameters: a = {a_fit}, b = {b_fit}, c = {c_fit}")

# Step 4: Visualize the results
plt.figure(figsize=(10, 6))

# Plot original data
plt.scatter(x_data, y_data, label='Data', color='red')

# Plot the fitted curve
x_fit = np.linspace(-10, 10, 1000)
y_fit = quadratic_model(x_fit, *params)
plt.plot(x_fit, y_fit, label='Fitted curve', color='blue')

# Add title and labels
plt.title('Curve Fitting Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show plot
plt.show()
