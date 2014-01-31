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

radial_nodes = 0
zeros = 1

# Define the base plot.
fig = plt.figure()
ax = list()

# Loop over the desired angular nodes.
cnt = 0
pixcnt = 0
plt.ion()
for t in np.r_[0:2*np.pi:20j]:
    cnt = 0
    pixcnt += 1
    for i in np.r_[0:radial_nodes+1:1]:
        for j in np.r_[1:zeros+1:1]:
            cnt += 1; #print cnt
            ax.append(fig.add_subplot(radial_nodes+1,zeros,cnt,projection='3d'))
            z = np.array([drumhead_height(i, j, r, theta, t) for r in radius])
            ax[-1].set_xlabel('R@%d,A@%d' % (i,j))
            ax[-1].plot_surface(x,y,z,rstride=1,cstride=1,cmap=mpl.cm.jet,linewidth=0)
            ax[-1].set_zlim(-1,1)
    plt.savefig('./disk-modes-%d.png' % pixcnt, format='png')
    plt.draw()
    plt.show()

