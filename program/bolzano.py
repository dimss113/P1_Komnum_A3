import matplotlib.pyplot as plt
import numpy as np
import math 

xl = float(input('lower x: '))
xu = float(input("upper x: "))
iterate = int(input("iteration: "))
x = 1.269
error_tolerate = 0.05;

list_of_xr = np.zeros(iterate)
list_iterate = np.arange(1, iterate+1, 1)

def function(x):
    return math.pow(x, 2) * 9*x - 13

def bisection():
    global xl, xu
    Fupper = function(xu)
    Flower = function(xl)
    xr = (xl + xu)/2
    xl, xu = interval_check(Fupper, Flower, xr)
    return xr;

def bisection_method():
    global xl, xu
    for i in range(iterate):
        xr = bisection()
        list_of_xr[i] = xr
        et = (x-xr)/x
        if((et <= error_tolerate) or round(xr, 3) == x):
            print(f"factor: {xr}")
        print(f"{xr} and {x}")
        print(f"et: {et}")
    
def interval_check(Fupper, Flower, xr):
    global xl, xu
    if(Fupper * Flower) < 0:
        xu = xr
        return xl, xu
    elif(Fupper * Flower) > 0:
        xl = xr
        return xl, xu
    else:
        return xr, xr


bisection_method()


plt.title("xr result")
plt.xlabel("iteration")
plt.ylabel("Result of xr")
plt.plot(list_iterate, list_of_xr)
plt.show()
