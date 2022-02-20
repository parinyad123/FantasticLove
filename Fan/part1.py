from timeit import repeat
import numpy as np
from pandas import Interval
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter 
def model(z, t):

    m = z[0]
    w = z[1]

    a = 0
    b = 2
    c = -1
    d = 0
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

# initial condition
z0 = [0,1]
# number of time points
n = 10000
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
    # print(m[i], w[i])

    z0 = z[1]

# print(len(m))
# print(len(w))
# xlim1 = -1.2
# xlim2 = 1.2
# ylim1 = -1.7
# ylim2 =1.7
fig, ax = plt.subplots()
# ax.set_xlim(xlim1, xlim2)
# ax.set_ylim(ylim1, ylim2)
ax.set_ylabel('w(t)')
ax.set_xlabel('m(t)')
ax.set_title('Part1')
ax.axhline(color='k', lw=0.8, ls='--')
ax.axvline(color='k', lw=0.8, ls='--')
l = plt.plot(m,w)

redDot, = plt.plot([m[0]], [w[0]], 'ro')

def animate(i):
    # print(i)

    redDot.set_data(m[i], w[i])
    return redDot,

myAnimation = FuncAnimation(fig, animate, frames=range(0,1000),\
            interval=10,blit=True, repeat=True)
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)
plt.show()
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)