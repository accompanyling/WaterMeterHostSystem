# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
# plt.style.use('seaborn-pastel')
#
#
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
# line, = ax.plot([], [], lw=3)
#
# def init():
#     line.set_data([], [])
#     return line,
# def animate(i):
#     x = np.linspace(0, 4, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,
#
# anim = FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)
#
# anim.save('sine_wave.html', writer='imagemagick')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sqlite3
import time

#figsize=(15, 6),
duration = time.strftime("%Y-%m-%d", time.localtime())
fig = plt.figure("用水实验记录",figsize=(10, 6),facecolor='#B5E1E1', frameon=True)
# creating a subplot
ax1 = fig.add_subplot(1, 1, 1)
t=0

def animate(i):
    xs = []
    print(i)
    conn = sqlite3.connect("fitdatas_test.db")
    c = conn.cursor()
    list1 = []
    c.execute("SELECT num FROM user_17754928919")
    res = c.fetchall()
    for m in res:
        list1.append(m[0])
    list1 = list1[1:]
    for k in range(len(list1)):
        xs.append(k + 1)
    conn.commit()
    conn.close()

    # if i>=len(list1):
    #     i=len(list1)
    ax1.clear()

    tmp1=list1[:i]
    tmp=tmp1
    ax1.plot(xs[:i], tmp,color='#111513', marker='o')
    plt.title('用户17754928919 %s用水情况'%duration,fontproperties='SimHei', fontsize=20, color="#3F8A8A")
    plt.xlabel('时间间隔', fontproperties='SimHei', fontsize=14, color="#3F8A8A")
    plt.ylabel('用水量(L)', fontproperties='SimHei', fontsize=14, color="#3F8A8A")
    plt.xticks(np.arange(len(xs[:i])), np.arange(len(xs[:i])) + 1, fontsize=1)
    # plt.xticks(np.linspace(1,int(len(values)+10),1),fontsize=12)
    if i>2:
        plt.yticks(np.linspace(0, max(tmp), 10), fontsize=12)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#6495ED')
    ax.spines['left'].set_color('#6495ED')
    ax.tick_params(which='major', width=2, color='#6495ED')
    ax.yaxis.grid(color='#B5E1E1', linestyle='--', linewidth=1, alpha=0.5)
    ax.xaxis.grid(color='#B5E1E1', linestyle='--', linewidth=1, alpha=0.5)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
# plt.style.use('dark_background')
#
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 31), ylim=(0, 150))
# line, = ax.plot([], [], lw=2)
#
#
# # initialization function
# def init():
#     # creating an empty plot/frame
#     line.set_data([], [])
#     return line,
#
#
# # lists to store x and y axis points
# xdata, ydata = [], []
#
#
# # animation function
# def animate(i):
#     # t is a parameter
#
#     # x, y values to be plotted
#
#     x=np.arange(1,31)
#     y = np.array(list1)
#
#     # appending new points to x, y axes points list
#     xdata.append(x)
#     ydata.append(y)
#     line.set_data(xdata, ydata)
#     return line,
#
#
# # setting a title for the plot
# plt.title('用户13028390277 2019-5-11用水情况')
# # hiding the axis details
# plt.axis('off')
#
# # call the animator
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=500, interval=20, blit=True)
#
# # save the animation as mp4 video file
# anim.save('dynamic.html', writer='imagemagick')
