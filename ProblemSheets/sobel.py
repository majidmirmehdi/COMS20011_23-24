# for python 2 compatibility #
from __future__ import print_function
#                            #
import numpy as np
from skimage import io
from scipy import signal
import matplotlib.pyplot as plt
# %matplotlib inline

# Sobel edge detection
A = io.imread('house.gif')

fig0 = plt.figure()
ax0  = fig0.add_subplot( 111 )
ax0.imshow( A, cmap=plt.cm.gray )
ax0.axis('off')
fig0.colorbar(ax0.imshow(A, cmap='gray'), ax=ax0)


fx = np.matrix( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
fy = np.matrix( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ] )
gx = signal.convolve2d( np.array(A, dtype=float), np.array(fx, dtype=float) ) / 8
gy = signal.convolve2d( np.array(A, dtype=float), np.array(fy, dtype=float) ) / 8
mag = np.sqrt( np.square(gx) + np.square(gy) )
ang = np.arctan( gy / gx )

# plot magnitude
fig1 = plt.figure()
ax1  = fig1.add_subplot( 111 )
ax1.imshow( mag, cmap=plt.cm.gray )
ax1.axis('off')
fig1.colorbar(ax1.imshow(mag, cmap='gray'), ax=ax1)

# plot angle
fig2 = plt.figure()
ax2  = fig2.add_subplot( 111 )
ax2.imshow( ang, cmap=plt.cm.gray )
ax2.axis('off')
fig2.colorbar(ax2.imshow(ang, cmap='gray'), ax=ax2)

plt.show()
