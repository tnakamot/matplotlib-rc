import numpy as np
import matplotlib.pyplot as plt

plt.style.use('../styles/tnakamot_engineering.mplstyle')

x   = np.linspace(0, np.pi * 4.0, 50)
x_ticks      = np.linspace(0, np.pi * 4.0, 5)
x_ticklabels = ['0'] + [r'$\pi$'] + [r'$%d \pi$' % (i) for i in range(2, 5)]

sin  = np.sin(x)
cos  = np.cos(x)
sin2 = sin**2
cos2 = cos**2

fig = plt.figure()
ax  = fig.add_subplot(1, 1, 1)
ax.set_title('Axes Title')
ax.plot(x, sin , label = r'$\mathrm{sin} \theta$'     , linestyle = '-', marker = 'o')
ax.plot(x, cos , label = r'$\mathrm{cos} \theta$'     , linestyle = '-', marker = 'v')
ax.plot(x, sin2, label = r'$\mathrm{sin}^2 \theta$'   , linestyle = '-', marker = 's')
ax.plot(x, cos2, label = r'$\mathrm{cos}^2 \theta$'   , linestyle = '-', marker = 'x')
ax.set_xlabel(r'$\theta $ [rad]')
ax.set_ylabel(r'Functions')
ax.set_xlim( (np.min(x), np.max(x) ) )
ax.set_xticks( x_ticks )
ax.set_xticklabels( x_ticklabels )
ax.set_ylim( (-1.0, 1.0) )
ax.legend()

fig.savefig('example1.pdf')
fig.savefig('example1.png')
fig.savefig('example1.svg')

plt.show()
