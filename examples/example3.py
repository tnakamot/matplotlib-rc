from scipy.special import jv 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('../styles/tnakamot_engineering.mplstyle')

x      = np.linspace(0, 15, 100)
orders = np.arange(0, 8)

J      = np.zeros( ( np.size(x), np.size(orders) ) )
labels = []
for order in orders:
    J[:,order] = jv(order, x)
    labels.append(r'$J_%d$' % order)

fig = plt.figure()
ax  = fig.add_subplot(1, 1, 1)
lines = ax.plot( x, J )

ax.set_title('Bessel function of the first kind')
ax.set_xlabel( r'$x$' )
ax.set_ylabel( 'Functions' )
ax.set_xlim( (np.min(x), np.max(x)) )
ax.set_ylim( (-0.6, 1.0) )
ax.legend( lines, tuple(labels), ncol = 2 )

fig.savefig('example3.pdf')
fig.savefig('example3.png')
fig.savefig('example3.svg')

plt.show()
