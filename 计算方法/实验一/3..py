from scipy.interpolate import interp1d
import pylab as plt
import numpy as np
T = np.array([700,720,740,760,780])
V=np.array([0.0977,0.1218,0.1406,0.1551,0.1664])
s3=interp1d(T,V,'cubic')
s=interp1d(T,V)
x=[750,770]
y1=s3(x);print('三次样条预测=',y1)
y2=s(x);print('分段线性插值=',y2)
x=np.linspace(700,780,81)
y3=s3(x);y4=s(x)
plt.rc('font', family='SimHei')
plt.plot(x,y3,'*-', label='三次样条插值')
plt.plot(x,y4,'-', label='分段线性插值')
plt.legend()
plt.show()