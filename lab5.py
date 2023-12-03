import numpy as np
import random

import pandas as pd
import pandas as pnd
from matplotlib import pyplot as ppt


def check_input(message):
    inp = -1
    try:
        inp = int(input(message))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, повторите!")
    return inp


def task1():
    pi = 3.1415926535
    a = 0.3
    b = -21.17
    y = np.power(1 / np.tan(pi / 4 - 1), 4) + np.power(a + 1.5, 1 / 3) - b / np.arcsin(np.power(np.abs(a), 2))
    print(y)

def task2():
    N = 3
    x_list = []
    for i in range(12):
        x_list.append([1, random.randint(N, N + 12), random.randint(60, 82)])
    x = np.array(x_list, dtype=int)
    y = np.random.randint(135, 186, (12, 1)) / 10
    print(x)
    print(y)
    a = (np.linalg.inv((np.transpose(x)) @ x)) @ (np.transpose(x) @ y)
    print(a)
    ax_0_list = []
    ax_1_list = []
    ax_2_list = []
    for i in range(12):
        ax_0_list.append(x[i, 0]*a[0])
        ax_1_list.append(x[i, 1]*a[1])
        ax_2_list.append(x[i, 2]*a[2])
        print(x[i, 1])
    ax_0 = np.array(ax_0_list)
    ax_1 = np.array(ax_1_list)
    ax_2 = np.array(ax_2_list)
    y1 = np.add(ax_0, ax_1, ax_2)
    print(y1)

def task3():
    dataset = pnd.read_csv("test.csv", delimiter=",", nrows=1000)
    # print(dataset.describe())
    # print(dataset["LifeSquare"].mean)
    if dataset.isnull().empty:
        print("Данные не имеют пропусков")
    else:
        print("Данные имеют пропуски:")
        print(dataset.isnull().sum())
        fig, ax = ppt.subplots()
        ppt.yscale(value='log')
        #
        ax.boxplot(dataset["Square"])
        ppt.show()

        dataset["Square"].plot(kind='hist')
        ppt.show()
        dataset = dataset.query("Square<100")
        dataset = dataset.query("Square>10")
        dataset = dataset.query("Rooms>0")
        # фильтр по значению

        fig, ax = ppt.subplots()
        ax.boxplot(dataset["Square"])
        ppt.show()

        new_ds = dataset.interpolate(method='linear', limit_direction='forward')
        print(new_ds.isnull().sum())
        print("Пропущенные данные были заполнены!")

        print(f"Количество квартир - {new_ds['Rooms'].value_counts()}")


def f(t):
    return np.log(np.abs(1.3 - t)) - np.exp(t)