import numpy as np
import matplotlib.pylab as plt


plt.ion()
fig, ax = plt.subplots()


x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

# ссылка на объект line2d который отвечает за отображение графика на координатных осях
line, = ax.plot(x, y)



for delay in np.arange(0, 2 * np.pi, 0.1):
    y = np.cos(x + delay)

    line.set_ydata(y)

    plt.draw()
    # для обработки внутренних событий и окна
    plt.gcf().canvas.flush_events()


plt.show()