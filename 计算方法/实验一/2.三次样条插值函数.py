from scipy.interpolate import interp1d
from scipy.integrate import quad
import scipy as sp
import numpy as np
y = lambda x: (3 * x ** 2 + x * 4 + 6) * np.sin(x)/(x ** 2 + 8 * x + 6)
x = np.linspace(0, 10, 1000)
y1 = y(x)
y2 = interp1d(x, y1, 'cubic')
y3 = y2(x)
I = quad(y, 0, 10)
print(I)
I2 = np.trapz(y3, x)
print(I2)
