import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(z, t):

    m = z[0]
    w = z[1]

    a = 0
    b = 2
    c = -1
    d = -3
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

# initial condition
z0 = [0,2]
# number of time points
n = 1000
# time point
t = np.linspace(0,100,n)
# store solution
m = np.empty_like(t)
w = np.empty_like(t)
# record initial conditions
m[0] = z0[0]
w[0] = z0[1]

# solve ODE
for i in range(1,n):
    tspan = [t[i-1], t[i]]

    z = odeint(model,z0, tspan)

    m[i] = z[1][0]
    w[i] = z[1][1]

    z0 = z[1]

# print(m)
# print(w)

plt.plot(m,w)
plt.show()