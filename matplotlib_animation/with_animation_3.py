import numpy as np
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation


def update_cos(frame, line, x):
    """

    :param frame:  параметр, который меняется от кадра к кадру. В данном случае начальная фаза (угол)
    :param line:   ссылка на объект Line2D
    :param x:
    :return: [line]
    """
    line.set_ydata(np.cos(x + frame))
    return [line]


fig, ax = plt.subplots()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

phasa = np.arange(0, 4 * np.pi, 0.1)

# ссылка на объект line2d который отвечает за отображение графика на координатных осях
line, = ax.plot(x, y)

animation = FuncAnimation(
    fig,  # фигура, где отображается анимация
    func=update_cos,  # функция обновления текущего кадра
    frames=phasa,  # параметр, меняющийся от кадра к кадру
    fargs=(line, x),  # дополнительные параметры для функции update_cos
    interval=30,  # задержка между кадрами в мс
    blit=True,  # использовать ли двойную буферизацию (обновление происходит незаметно для пользователя)
    repeat=False)  # зацикливать ли анимацию

plt.show()
