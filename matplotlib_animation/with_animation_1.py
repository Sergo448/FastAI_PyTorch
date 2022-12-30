import time
import numpy as np
import matplotlib.pylab as plt

plt.ion()

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)

for delay in np.arange(0, 2 * np.pi, 0.1):
    y = np.cos(x + delay)

    plt.clf()
    plt.plot(x, y)

    plt.draw()
    # для обработки внутренних событий и окна
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)

plt.ioff()
plt.show()