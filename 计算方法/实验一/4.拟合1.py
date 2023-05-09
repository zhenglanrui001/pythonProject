import numpy as np
T=np.arange(8)
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8])
p=np.vstack([T,np.ones(8)]).T
a=np.linalg.pinv(p)@y
print(a)

import numpy as np
T=np.arange(8)
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8])
a=np.polyfit(T,y,1)
print(a)