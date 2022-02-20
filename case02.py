import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
selectcase = 2.2

# case 1: b>0, c<0
if selectcase == 1:
    pass

# case 2: b>0, c<0, d<0
elif selectcase == 2.1:
    #  |d|**2 > 4b|c| 
    b = 1
    c = 1
    d = 3
    lambda1 = (-d+np.sqrt((d**2)-(4*b*c)))/2
    lambda2 = (-d-np.sqrt((d**2)-(4*b*c)))/2
    eigen_v1 = [1, lambda1/b]
    eigen_v2 = [1, lambda2/b]

    xlim1 = -5
    xlim2 = 5
    ylim1 = -5
    ylim2 = 5

elif selectcase == 2.2:
    b = 2
    c = 2
    d = 4
    lambda1 = -d/2
    lambda2 = lambda1
    eigen_v1 = [1, lambda1/b]
    eigen_v2 = [1, lambda2/b]

    xlim1 = -5
    xlim2 = 5
    ylim1 = -5
    ylim2 = 5
elif selectcase == 2.3:
    b = 1
    c = 1
    d = 3
    lambda1 = (-d+np.sqrt((d**2)-(4*b*c)))/2
    lambda2 = (-d-np.sqrt((d**2)-(4*b*c)))/2
    eigen_v1 = [1, lambda1/b]
    eigen_v2 = [1, lambda2/b]

    xlim1 = -5
    xlim2 = 5
    ylim1 = -5
    ylim2 = 5

fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
ax = plt.axes()
ln, = ax.plot([], [], 'bo')
m_t, w_t = [], []
t_t = []
m0 = cmath.exp(lambda1*0)*eigen_v1[0] + cmath.exp(0*lambda2)*eigen_v2[0]
w0 = cmath.exp(lambda1*0)*eigen_v1[1] + cmath.exp(0*lambda2)*eigen_v2[1]
def init():
    ax.set_xlim(xlim1, xlim2)
    ax.set_ylim(ylim1, ylim2)
    ax.axhline(color='k', lw=0.8, ls='--')
    ax.axvline(color='k', lw=0.8, ls='--')
    return ln,

def loverpath(time):
    # print("time=", time)
    m = cmath.exp(lambda1*time)*eigen_v1[0] + cmath.exp(time*lambda2)*eigen_v2[0] 
    
    # m = m-m0
    # m_t.append(m.real)
    m_t.append(abs(m))

    w = cmath.exp(lambda1*time)*eigen_v1[1] + cmath.exp(time*lambda2)*eigen_v2[1]
    # w=w-w0
    # w_t.append(w.real)
    w_t.append(abs(w))
    # t_t.append(w.real+1)
    # ln.set_data([m_t, w_t],[w_t, w_t])
    ln.set_data(m_t, w_t)
    # print("time=", time, m.real,w.real)
    print("time=", time, abs(m), abs(w))
    # print(m,w)
    return ln,

anim = FuncAnimation(fig, loverpath, 
                    frames =  [t*.05 for t in range(0,10000)],
                    interval=10,
                    init_func=init, blit=True)
plt.show()
# anim.save('animation.gif', writer='imagemagick', fps=120)