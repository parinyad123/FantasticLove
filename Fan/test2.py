import numpy as np
import pylab as plt
import matplotlib.animation as anim

fig, axes = plt.subplots(1,3,figsize=(18,6))
# print(fig, axes)
# ims   = []
im1   = [ax.plot([],[])[0] for ax in axes]
im2   = [ax.plot([],[])[0] for ax in axes]
print(im1)
x = np.arange(0,2*np.pi,0.1)
# 
# legs = [ax.legend(loc=2, prop={'size': 6})  for ax in axes]
# print(legs)
for ax in axes:
    ax.set_xlim([0,2*np.pi])
    ax.set_ylim([-1,1])
plt.tight_layout()
n=50
def update(i):
    for sp in range(3):
        y1 = np.sin((sp+1)*x + (i)*np.pi/n)
        y2 = np.cos((sp+1)*x + (i)*np.pi/n)

        im1[sp].set_data(x,y1)
        im2[sp].set_data(x,y2)

        # lab = 'i='+str(i)+', sp='+str(sp+1)
        # legs[sp].texts[0].set_text(lab)
        # legs[sp].texts[1].set_text(lab)
    print("-----------")
    # print(im1 + im2 +legs)
    # return im1 + im2 +legs 
    return im1 + im2  

ani = anim.FuncAnimation(fig,update, frames=n,blit=True)
plt.show()