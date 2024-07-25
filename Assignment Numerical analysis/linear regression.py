import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate the data
# True parameters
m_true = 2.5
c_true = 1.3

# Generate x values
x_data = np.linspace(0, 10, 100)

# Generate y values with some noise
np.random.seed(42)  # For reproducibility
y_data = m_true * x_data + c_true + np.random.normal(0, 2, size=x_data.shape)

# Step 2: Perform linear regression using the least squares method
# Create the design matrix X (with a column of ones for the intercept)
X = np.vstack([x_data, np.ones(len(x_data))]).T

# Perform the least squares calculation
# beta = (X^T * X)^-1 * X^T * y
beta = np.linalg.inv(X.T @ X) @ X.T @ y_data
m_fit, c_fit = beta

print(f"Fitted parameters: m = {m_fit}, c = {c_fit}")

# Step 3: Visualize the results
plt.figure(figsize=(10, 6))

# Plot original data
plt.scatter(x_data, y_data, label='Data', color='red')

# Plot the fitted line
y_fit = m_fit * x_data + c_fit
plt.plot(x_data, y_fit, label='Fitted line', color='blue')

# Add title and labels
plt.title('Linear Regression Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show plot
plt.show()

