from scipy.integrate import quad

# Define the function to integrate
def integrand(x):
    return x**2

# Compute the integral from 0 to 10
result, error = quad(integrand, 0, 10)

print(f"Integral result: {result}")
print(f"Estimate of error: {error}")
