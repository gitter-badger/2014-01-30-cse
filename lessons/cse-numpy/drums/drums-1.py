from __future__ import division
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import jn, jn_zeros

def drumhead_height(n, k, distance, angle, t):
    nth_zero = jn_zeros(n, k)
    return np.cos(t)*np.cos(n*angle)*jn(n, distance*nth_zero[-1])

# Define polar and cartesian coordinates for the drum.
theta  = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r*np.cos(theta) for r in radius])
y = np.array([r*np.sin(theta) for r in radius])

radial_nodes  = 3
zeros = 3

# Define the base plot.
fig = plt.figure()

# Display the desired angular nodes.
ax = fig.add_subplot(1,1,1,projection='3d')
z = np.array([drumhead_height(radial_nodes, zeros, r, theta, 0.5) for r in radius])
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=mpl.cm.jet)

plt.show()

