import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image

from numpy import array


def median_filter(data, filter_size):
    temp = []
    indexer = int(filter_size) // 2
    data_final = []
    data_final = numpy.zeros((len(data), len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []

    # data - начальный массив пискелей
    # data_final - массив после наложения меедианного фидльтра

    return data_final


def main():
    img = Image.open("03.jpg").convert("L")
    # изображение в папке проекта
    arr = numpy.array(img)
    size = int(input('Enter median filter size-'))
    removed_noise = median_filter(arr, size)
    img = Image.fromarray(removed_noise)
    img.show()

    a = array(removed_noise)

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            removed_noise[i][j] -= 225

    high = a.shape[0]
    width_init = a.shape[1]
    width = int(input("Input width /4- "))
    delta = int(input("Input step- "))
    mu = 0
    mu_arr = []
    var = 0
    print("high =", high)
    print("width =", width_init)

    var1 = (width_init // delta) - (width/delta)

    while var1 > len(mu_arr):
        mas = list(range(var, width))
        for i in range(high):
            for j in mas:
                if j >= (width / 2):
                    mu += removed_noise[i][j]
                else:
                    mu -= removed_noise[i][j]

        mu_arr.append(mu)
        var += delta
        width += delta
        mu = 0

    plt.plot(mu_arr)
    plt.show()


main()
