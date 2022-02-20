# Import Libraries

from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Create figure and subplot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 

# Define and update plot
# while True:
for i in range(50):
    ax.set_xlim(0, 200)
    ax.plot(i, 2, marker='o', color='blue')
    # display(fig)    
    clear_output(wait = True)
    plt.pause(0.01)
  
plt.show()