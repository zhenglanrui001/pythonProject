import numpy as np
from scipy.interpolate import lagrange
x0 = np.arange(1, 7)
y = np.array([16, 18, 21, 17, 15, 12])
a = lagrange(x0, y)
print(a)
yh = np.polyval(a, [1.5, 2.6])
print(yh)