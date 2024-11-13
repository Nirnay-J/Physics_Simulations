import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Constant
l = 1
g = 9.8
amplitude_theta = np.pi/4
phase = np.pi/4

def position(t):
	theta = amplitude_theta*np.sin(np.sqrt(g/l)*t+phase)
	pos = [l*np.sin(theta),-l*np.cos(theta)]
	return pos

t_range = np.linspace(0,10,1000)
positions = np.array([position(t) for t in t_range])
x_pos = [i[0] for i in positions]
y_pos = [i[1] for i in positions]

plt.scatter(x_pos,y_pos)
plt.show()
