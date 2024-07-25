import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev

# Generate some data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Perform spline interpolation
spl = splrep(x, y)
xnew = np.linspace(0, 10, 200)
ynew = splev(xnew, spl)

# Plot the data and the spline interpolation
plt.scatter(x, y, label='Data')
plt.plot(xnew, ynew, label='Spline interpolation', color='red')
plt.legend()
plt.show()
