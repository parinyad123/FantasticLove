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
    b = 1
    c = 1
    d = -3
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

# initial condition
z01 = [0,1]
z02 = [1,0]
# number of time points
n = 1000
# time point
t = np.linspace(0,6,n)
# store solution
m1 = np.empty_like(t)
w1 = np.empty_like(t)
m2 = np.empty_like(t)
w2 = np.empty_like(t)
# record initial conditions
m1[0] = z01[0]
w1[0] = z01[1]
m2[0] = z02[0]
w2[0] = z02[1]
# solve ODE
for i in range(1,n):
    tspan = [t[i-1], t[i]]

    z1 = odeint(model,z01, tspan)
    z2 = odeint(model, z02,tspan)
    m1[i] = z1[1][0]
    w1[i] = z1[1][1]
    m2[i] = z2[1][0]
    w2[i] = z2[1][1]
    # print(m[i], w[i])

    z01 = z1[1]
    z02 = z2[1]

# print(len(m))
# print(len(w))

fig, ax = plt.subplots()
ax.set_ylabel('w(t)')
ax.set_xlabel('m(t)')
ax.set_title('Part4-1')
ax.axhline(color='k', lw=0.8, ls='--')
ax.axvline(color='k', lw=0.8, ls='--')
plt.plot(m1,w1)
plt.plot(m2,w2)

redDot1, = plt.plot([m1[0]], [w1[0]], 'ro')
redDot2, = plt.plot([m2[0]], [w2[0]], 'go')
def animate(i):
    # print(i)

    redDot1.set_data(m1[i], w1[i])
    redDot2.set_data(m2[i], w2[i])
    return redDot1,redDot2

myAnimation = FuncAnimation(fig, animate, frames=range(0,1000),\
            interval=.5,blit=True, repeat=True)
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)
plt.show()
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)