import numpy as np
import matplotlib.pylab as plt
from matplotlib.animation import ArtistAnimation


fig = plt.figure(figsize=(10, 6))
# 3-х мерная координатная ось
ax_3d = fig.add_subplot(projection='3d')


x = np.arange( -2 * np.pi, 2 * np.pi, 0.2)
y = np.arange( -2 * np.pi, 2 * np.pi, 0.2)
# сетка для отображения 3-х мерного графика
xgrid, ygrid = np.meshgrid(x, y)

phasa = np.arange(0, 2 * np.pi, 0.1)
# список кадров
frames: list = []

# цикл для перебора фазы
for p in phasa:
    zgrid = np.sin(xgrid + p) * np.sin(ygrid) / (xgrid * ygrid)
    # строим 3-х мерный график
    line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
    # сохраняем список объектов текущих кадров
    frames.append([line])

animation = ArtistAnimation(
    fig,             # фигура, где отображается анимация
    frames,    # параметр, меняющийся от кадра к кадру
    interval=30,     # задержка между кадрами в мс
    blit=True,       # использовать ли двойную буферизацию (обновление происходит незаметно для пользователя)
    repeat=True)    # зацикливать ли анимацию


plt.show()
