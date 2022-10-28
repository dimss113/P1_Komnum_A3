import numpy as np
import matplotlib.pyplot as plt
import math

xl = float(input("masukkan x lower: "))
xu = float(input("masukkan x upper: "))
iterate = int(input("masukkan jumlah interasi: "))
xt = 1.26611328125


list_xr = list()
list_iterate = list()

def function(x):
    return x*x + 9*x - 13

def bisection():
    global xl, xu
    for i in range(iterate):
        xr = (xl+xu)/2
        list_xr.append(xr)
        list_iterate.append(i+1)
        
        print(f"iterasi ke - {i+1}")
        print(f"xu dan xl: {xu} || {xl}")
        print(f"xr dan xt: {xr} || {xt}")

        et = round(math.fabs((xt-xr)/xt), 5)
        print(f"et: {et}\n")

        fxl = function(xl)
        fxr = function(xr)

        mul = round(fxl * fxr, 3)
        if(mul == 0):
            print(f"hasil faktor: {xr} ")
            return
        elif (mul) < 0:
            xu = xr
        elif mul > 0:
            xl = xr

bisection()
x_point = np.linspace(-50, 40, 100);
y_point = function(x_point)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.spines['left'].set_position('zero')
ax1.spines['bottom'].set_position('zero')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.plot(x_point, y_point, 'g')

ax2 = fig.add_subplot(2, 1, 2)
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('center')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
plt.plot(list_iterate, list_xr)

plt.show()