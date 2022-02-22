from timeit import repeat
import numpy as np
from pandas import Interval
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter 
def model1(z, t):

    m = z[0]
    w = z[1]

    a = 0
    b = 1
    c = -1
    d = 3
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

def model2(z, t):
    
    m = z[0]
    w = z[1]

    a = 0
    b = 2
    c = -2
    d = 4
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

def model3(z, t):
    
    m = z[0]
    w = z[1]

    a = 0
    b = 6
    c = -6
    d = 1
    dmdt = a*m + b*w
    dwdt = c*m + d*w
    return [dmdt, dwdt]

# initial condition
z01 = [0,1]
z02 = [1,0]

z03 = [0,1]
z04 = [1,0]

z05 = [0,1]
z06 = [1,0]

# number of time points
n = 1000
# time point
t = np.linspace(0,1,n)

# store solution
m1 = np.empty_like(t)
w1 = np.empty_like(t)
m2 = np.empty_like(t)
w2 = np.empty_like(t)

m3 = np.empty_like(t)
w3 = np.empty_like(t)
m4 = np.empty_like(t)
w4 = np.empty_like(t)

m5 = np.empty_like(t)
w5 = np.empty_like(t)
m6 = np.empty_like(t)
w6 = np.empty_like(t)

# record initial conditions
m1[0] = z01[0]
w1[0] = z01[1]
m2[0] = z02[0]
w2[0] = z02[1]

m3[0] = z03[0]
w3[0] = z03[1]
m4[0] = z04[0]
w4[0] = z04[1]

m5[0] = z05[0]
w5[0] = z05[1]
m6[0] = z06[0]
w6[0] = z06[1]
# solve ODE
for i in range(1,n):
    tspan = [t[i-1], t[i]]

    z1 = odeint(model1, z01, tspan)
    z2 = odeint(model1, z02, tspan)
    z3 = odeint(model2, z03, tspan)
    z4 = odeint(model2, z04, tspan)
    z5 = odeint(model3, z05, tspan)
    z6 = odeint(model3, z06, tspan)

    m1[i] = z1[1][0]
    w1[i] = z1[1][1]
    m2[i] = z2[1][0]
    w2[i] = z2[1][1]
    z01 = z1[1]
    z02 = z2[1]

    m3[i] = z3[1][0]
    w3[i] = z3[1][1]
    m4[i] = z4[1][0]
    w4[i] = z4[1][1]
    z03 = z3[1]
    z04 = z4[1]

    m5[i] = z5[1][0]
    w5[i] = z5[1][1]
    m6[i] = z6[1][0]
    w6[i] = z6[1][1]
    z05 = z5[1]
    z06 = z6[1]

# print(len(m))
# print(len(w))

fig, ax = plt.subplots(1,3,figsize=(15,6))
fig.subplots_adjust(left=0.05, bottom=0.1, right=.98, top=.9)
# ax.set_ylabel('w(t)')
# ax.set_xlabel('m(t)')
# ax.set_title('Part2-1')
ax[0].set_ylabel('w(t)')
for i in range(3):
    ax[i].margins()
    ax[i].axhline(color='k', lw=0.8, ls='--')
    ax[i].axvline(color='k', lw=0.8, ls='--')
    
    ax[i].set_xlabel('m(t)')
    ax[i].set_title('Part2-{}'.format(i+1))
# plt.plot(m1,w1)
# plt.plot(m2,w2)
ax[0].plot(m1,w1)
ax[0].plot(m2,w2)
ax[1].plot(m3,w3)
ax[1].plot(m4,w4)
ax[2].plot(m5,w5)
ax[2].plot(m6,w6)

redDot1, = ax[0].plot([m1[0]], [w1[0]], 'ro')
redDot2, = ax[0].plot([m2[0]], [w2[0]], 'go')
redDot3, = ax[1].plot([m3[0]], [w3[0]], 'ro')
redDot4, = ax[1].plot([m4[0]], [w4[0]], 'go')
redDot5, = ax[2].plot([m5[0]], [w5[0]], 'ro')
redDot6, = ax[2].plot([m6[0]], [w6[0]], 'go')
def animate(i):
    # print(i)

    redDot1.set_data(m1[i], w1[i])
    redDot2.set_data(m2[i], w2[i])
    redDot3.set_data(m3[i], w3[i])
    redDot4.set_data(m4[i], w4[i])
    redDot5.set_data(m5[i], w5[i])
    redDot6.set_data(m6[i], w6[i])
    return redDot1,redDot2,redDot3,redDot4,redDot5,redDot6

myAnimation = FuncAnimation(fig, animate, frames=range(0,1000),\
            interval=1,blit=True, repeat=True)
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)
plt.show()
# myAnimation.save('part1.gif', writer='imagemagick', fps=200)