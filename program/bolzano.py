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

print(list_xr)

plt.title("result")
plt.xlabel("iteration")
plt.ylabel("Result of xr")
plt.plot(list_iterate, list_xr)
plt.show()