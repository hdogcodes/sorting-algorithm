import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def sort(lis,colours):
    n = len(lis)
    for i in range(0, n-1):
        if lis[i] > lis[i+1]:
            lis[i] , lis[i+1] = lis[i+1] , lis[i]
            colours[[i, i+1]] = colours[[i+1, i]]
    return lis , colours

def checker(lis, n):
    if lis[n] < lis[n-1]:
        return n
    if n == 1:
        return len(lis)
    return checker(lis, n-1)

n = 30



datas = np.random.randint(1, 255, n)

colour = np.zeros((n,2))
bruh =  datas / 255
colour = np.column_stack((colour, bruh))
data = list(datas)

fig, ax = plt.subplots()
bars = ax.bar(range(len(data)), data, color= colour)
ax.set_ylim(0, 270)
def update(frame):
    sort(data,colour)
    if checker(data, len(data) - 1) == len(data):
        ani.event_source.stop()
    for bar, h, c in zip(bars, data, colour):
        bar.set_height(h)
        bar.set_color(c)
    ax.set_title(f"Pass {frame + 1}")
    return bars

ani = FuncAnimation(fig, update, frames=len(data) - 1,
                    interval=200, blit=False, repeat=False)

plt.show()













