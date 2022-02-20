import cmath
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
b = 8
c = 3
m_t = []
w_t = []

lambda1 = np.sqrt(b*c)*1j
eigen_v1 = [1, np.sqrt(c/b)*1j]
eigen_v2 = [1, np.sqrt(c/b)*-1j]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 

for t in range(0,100):
    t = t*.02
    m = cmath.exp(lambda1*t)*eigen_v1[0] + cmath.exp(-t*lambda1)*eigen_v2[0]
    m_t.append(m.real)
    # m_t.append(abs(m))

    w = cmath.exp(lambda1*t)*eigen_v1[1] + cmath.exp(-t*lambda1)*eigen_v2[1]
    w_t.append(w.real)
    # w_t.append(abs(w))

    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    ax.grid()
    ax.plot(m.real, w.real, marker='o', color='blue')
    # display(fig)    
    clear_output(wait = False)
    plt.pause(.5)

# plt.scatter(m_t, w_t)
# plt.grid()
plt.show()

