import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

b = 8
c = 3
lambda1 = np.sqrt(b*c)*1j
lambda2 = np.sqrt(b*c)*-1j
eigen_v1 = [1, np.sqrt(c/b)*1j]
eigen_v2 = [1, np.sqrt(c/b)*-1j]

fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
ax = plt.axes()
ln, = ax.plot([], [], 'bo')
m_t, w_t = [], []

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.5, 2.5)
    ax.axhline(color='k', lw=0.8, ls='--')
    ax.axvline(color='k', lw=0.8, ls='--')
    return ln,

def loverpath(time):
    m = cmath.exp(lambda1*time)*eigen_v1[0] + cmath.exp(time*lambda2)*eigen_v2[0]
    m_t.append(m.real)

    w = cmath.exp(lambda1*time)*eigen_v1[1] + cmath.exp(time*lambda2)*eigen_v2[1]
    w_t.append(w.real)
    ln.set_data(m_t, w_t)
    # print(m_t,w_t)
    return ln,

anim = FuncAnimation(fig, loverpath, 
                    frames =  [t*.02 for t in range(0,1000)],
                    interval=100,
                    init_func=init, blit=True)
plt.show()
# anim.save('animation.gif', writer='imagemagick', fps=120)