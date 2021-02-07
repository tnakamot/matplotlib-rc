import numpy as np
import matplotlib.pyplot as plt

x   = np.linspace(0, np.pi * 4.0, 1000)
x_ticks      = np.linspace(0, np.pi * 4.0, 5)
x_ticklabels = ['0'] + [r'$\pi$'] + [r'$%d \pi$' % (i) for i in range(2, 5)]

sin  = np.sin(x)
cos  = np.cos(x)
sin2 = sin**2
cos2 = cos**2

plt.style.use('../styles/tnakamot_engineering.mplstyle')

fig = plt.figure()

ax1  = fig.add_subplot(2, 1, 1)
ax1.set_title('Ax1')
ax1.plot(x, sin , label = r'$\mathrm{sin} \theta$', linestyle = '-')
ax1.plot(x, cos , label = r'$\mathrm{cos} \theta$', linestyle = '--')
ax1.set_xlabel(r'$\theta $ [rad]')
ax1.set_ylabel(r'Functions')
ax1.set_xlim( (np.min(x), np.max(x) ) )
ax1.set_xticks( x_ticks )
ax1.set_xticklabels( x_ticklabels )
ax1.set_ylim( (-1.0, 1.0) )
ax1.legend()

ax2  = fig.add_subplot(2, 1, 2)
ax2.set_title('Ax2')
ax2.plot(x, sin2, label = r'$\mathrm{sin}^2 \theta$', linestyle = ':')
ax2.plot(x, cos2, label = r'$\mathrm{cos}^2 \theta$', linestyle = '-.')
ax2.set_xlabel(r'$\theta $ [rad]')
ax2.set_ylabel(r'Functions')
ax2.set_xlim( (np.min(x), np.max(x) ) )
ax2.set_xticks( x_ticks )
ax2.set_xticklabels( x_ticklabels )
ax2.set_ylim( (0.0, 1.0) )
ax2.legend()

fig.savefig('example2.pdf')
fig.savefig('example2.png')
fig.savefig('example2.svg')

plt.show()
