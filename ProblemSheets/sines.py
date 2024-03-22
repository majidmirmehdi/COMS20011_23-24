# for python 2 compatibility #
from __future__ import print_function
#                            #
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(precision=4)
# interactive plotting
plt.ion()

# is the script run as standalone application i.e. `python tt.py`?
standalone = True

# ANSWER #
x = np.arange(-3, 3.1, 0.1)
n = [1/4.0, 1, 2] # add more factors to get more sines

s = []
for ni in n:
  s.append( np.sin(2*np.pi*x*ni) )

ss = sum(s)

## Plot the data
fig = plt.figure()
ax  = fig.add_subplot( 111 )
ax.plot(x, ss, color='r')
c = ['g', 'b', 'k', 'c', 'm', 'y']
for i, si in enumerate(s):
  ax.plot(x, si, color=c[i+3])
plt.draw()

plt.ioff()
if standalone:
  print("Close all the plots to exit...")
  plt.show()
