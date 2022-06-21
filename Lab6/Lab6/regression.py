import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

#регрессия первого порядка
def regression_equation(data):
    X = data[:-1]
    Y = data[1:]
    b = search_b(X, Y)
    a = search_a(X, Y, b)
    forecast = []

    for i in data:
        rand = random.randint(0, 4)
        if rand % 2 == 0:
           forecast.append(a + b * i + random.uniform(0, 0.01 * i))
        else:
           forecast.append(a + b * i - random.uniform(0, 0.01 * i))

    fig, ax = plt.subplots()  
    ax.plot(data);
    ax.plot(forecast);
    plt.show()

#поиск угла пересечения с осью линейной регрессии
def search_a(X, Y, b):
    a = 0
    for i in range(len(X)):
        a += Y[i] - b * X[i]
    return a / len(X)

#поиск угла наклона линейной регрессии
def search_b(X, Y):
    average_x = sum(X) / len(X)
    average_y = sum(Y) / len(Y)
    numenator = 0
    denominator = 0

    for i in range(len(X)):
        #ковариация
        numenator += (Y[i] - average_y) * (Y[i] - average_x)
        #дисперсия
        denominator += math.pow((X[i] - average_x), 2)

    return numenator / denominator

