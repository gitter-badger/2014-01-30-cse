from __future__ import division
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import jn, jn_zeros
import subprocess

def drumhead_height(n, k, distance, angle, t):
    nth_zero = jn_zeros(n, k)
    return np.cos(t)*np.cos(n*angle)*jn(n, distance*nth_zero[-1])

# Define polar and cartesian coordinates for the drum.
theta  = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r*np.cos(theta) for r in radius])
y = np.array([r*np.sin(theta) for r in radius])

radial_nodes = 2
zeros = 2

# Define the base plot.
fig = plt.figure(num=None,figsize=(16,16),dpi=120,facecolor='w',edgecolor='k')
ax = list()

# Loop over the desired angular nodes.
cnt = 0
pixcnt = 0
plt.ion()
for t in np.r_[0:2*np.pi:40j]:
    cnt = 0
    pixcnt += 1
    for i in np.r_[0:radial_nodes+1:1]:
        for j in np.r_[1:zeros+1:1]:
            cnt += 1;
            ax.append(fig.add_subplot(radial_nodes+1,zeros,cnt,projection='3d'))
            z = np.array([drumhead_height(i, j, r, theta, t) for r in radius])
            ax[-1].set_xlabel('R@%d,A@%d' % (i,j))
            ax[-1].plot_surface(x,y,z,rstride=1,cstride=1,cmap=mpl.cm.Accent,linewidth=0,vmin=-1,vmax=1)
            ax[-1].set_zlim(-1,1)
    plt.savefig('./drum-modes-%d.png' % pixcnt, format='png')

# Collate pictures to an animated GIF.
import os,string
cwd = os.getcwd()
cmd = 'cd %s; ls drum-modes*.png | sort -k1.12n'%cwd
png_files = os.popen(cmd)
png_files_list = string.join(png_files.readlines()).replace('\n',' ')
os.popen('convert -delay 10 -loop 1 %s ./drum-animate.gif'%png_files_list)

