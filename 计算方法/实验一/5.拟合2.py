import numpy as np
from scipy.optimize import curve_fit
xy=np.array([[6,2,6,7,4,2,5,9],[4,9,5,3,8,5,8,2]])
z0=np.array([5,2,1,9,7,4,3,3])
z=lambda t,a,b,c: a*np.exp(b*t[0]) +c*t[1]**2
p,xov = curve_fit(z,xy,z0)
print(p)