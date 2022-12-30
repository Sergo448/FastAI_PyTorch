import numpy as np
import matplotlib.pylab as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

plt.plot(x, y)
plt.show()