import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

#регрессия первого порядка
def regression_equation(data):
    X = data[:-1]
    Y = data[1:]
    a = search_a(X, Y)
    b = search_b(X, Y)
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

#ковариация
def cov(X, Y):
    average_x = sum(X) / len(X)
    average_y = sum(Y) / len(Y)
    numenator = 0
    for i in range(len(X)):
        numenator += (Y[i] - average_y) * (X[i] - average_x)

    return numenator / (len(X) - 1)

#диссперсия
def var(X, Y):
    average_x = sum(X) / len(X)
    numenator = 0
    for i in range(len(X)):
        numenator += math.pow((X[i] - average_x), 2)

    return numenator / len(X) 

#поиск угла пересечения с осью линейной регрессии
def search_a(X, Y):
    numerator = cov(X, Y)
    denominator = var(X, Y)
    return numerator / denominator

#поиск угла наклона линейной регрессии
def search_b(X, Y):
    average_x = sum(X) / len(X)
    average_y = sum(Y) / len(Y)
    numenator = 0
    denominator = 0

    for i in range(len(X)):
        numenator += (Y[i] - average_y) * (Y[i] - average_x)
        denominator += math.pow((X[i] - average_x), 2)

    return numenator / denominator
