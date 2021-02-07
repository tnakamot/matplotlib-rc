import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('../styles/tnakamot_engineering.mplstyle')
plt.style.use('https://raw.githubusercontent.com/tnakamot/matplotlib-rc/master/styles/tnakamot_engineering.mplstyle')

x  = np.linspace(-1.5, 1.5, 101)
ls = np.arange(2, 6)

sigmoid = np.zeros( ( np.size(x), np.size(ls) ) )
labels  = []
xytexts = [ (-1.3, -0.4),
            (-1.0,  0.0),
            (-0.8,  0.4),
            (-0.5,  0.8) ]
for i,l in enumerate(ls):
    sigmoid[:,i] = 2.0 / (1 + np.e ** (-l * x)) - 1
    labels.append(r'$\frac{2}{1 + e^{- %d x}} - 1$' % (l))

fig = plt.figure()
ax  = fig.add_subplot(1, 1, 1)
lines = ax.plot( x, sigmoid )

ax.set_title('Sigmoid function')
ax.set_xlabel( r'$x$' )
ax.set_ylabel( 'Functions' )
ax.set_xlim( (np.min(x), np.max(x)) )
ax.set_ylim( (-1.0, 1.0) )

for i, line in enumerate(lines):
    xydata = line.get_xydata()
    idx    = int( np.size(xydata, axis=0) * (i+1) / (len(lines) + 3) )
    xypts  = xydata[idx]
    ax.annotate(labels[i], xydata[idx], xytext=xytexts[i],
                fontsize        = 16,
                backgroundcolor = 'white',
                arrowprops      = dict(arrowstyle='-'))
    
fig.savefig('example4.pdf')
fig.savefig('example4.png')
fig.savefig('example4.svg')

plt.show()
