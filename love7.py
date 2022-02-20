import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
ax = plt.axes()
ln, = ax.plot([], [], 'bo')
xdata, ydata = [], []

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    # xdata = frame
    # ydata = np.sin(frame)
    ln.set_data(xdata, ydata)
    return ln,

anim = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), 
                    # interval=10,
                    init_func=init, blit=True)
plt.show()
# anim.save('animation.gif', writer='imagemagick', fps=120)