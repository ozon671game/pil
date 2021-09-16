import matplotlib.pyplot as plt
import numpy
import numpy as np

from numpy import array


arr = [[1,1,0,1,1,1,0,1,1,1,0,1],[0,0,1,1,1,1,0,1,1,1,0,1],[1,1,1,0,1,1,0,1,1,1,0,1],[0,0,0,0,1,1,0,1,1,1,0,1]]

a = array(arr)
mu = 0

print(a.shape)
h = a.shape[0]
w = a.shape[1]

width = 4
step = 2
var = 0

mu_arr = []
x = 0




while(len(mu_arr) < (w / step)-1):
    mas = list(range(var, width))
    print(mas)
    for i in range(h):
        for j in mas:
            if j >= width /2:
                mu += arr[i][j]
            else:
                mu -= arr[i][j]

    mu_arr.append(mu)
    var += step
    width += step
    x += 1
    mu = 0
    #mas = list(range(var, width))

print(x)
# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         if j >= 2:
#             mu += arr[i][j]
#         else:
#             mu -= arr[i][j]


print(mu_arr)
# plt.plot(mu)
# plt.show()
