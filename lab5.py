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

def task4():
    # s = ln|1,3 - t|-e^t, 2<=t<=3, dt = 0,03
    arguments = np.arange(2, 3, 0.03)
    print(arguments)
    list_of_values = []
    count = 0

    for i in arguments:
        list_of_values.append(f(i))
        print(f"Argument: {i}, Value: {f(i)}")
        count += 1
    values = np.array(list_of_values)
    print(f"Max: {values.max()}, Min : {values.min()} Mean: {values.sum()/count} Amount of elements: {count}")
    mean_line = (values.sum()/count) * np.ones(values.size)
    ppt.plot(arguments, values)
    ppt.ylabel("Ось Y: f(x)")
    ppt.xlabel("Ось X")
    ppt.plot(arguments, mean_line)
    ppt.show()


def z(choice, x, y):
    match choice:
        case 1:
            return np.power(x, 0.25) + np.power(y, 0.25)
        case 2:
            return x * x - y * y
        case 3:
            return 2 * x + 3 * y
        case 4:
            return x * x + y * y
        case 5:
            return 2 + 2 * x + 2 * y - x * x - y * y
        
def task5():
    arg = np.arange(2, 5, 0.5)
    arg1 = np.arange(0, 3, 0.5)
    choice = -1
    while choice != 0:
        print("\nВыберите:\n1.z = x^(2.5) + y^(2.5)"
              "\n2.z = x^2 - y^2"
              "\n3.z = 2x + 3y"
              "\n4.z = x^2 + y^2"
              "\n5.z = 2 + 2x + 2y - x^2 - y^2")
        while choice < 0 or choice > 5:
            choice = check_input("\nВаш выбор - ")
    list_of_values = []

    for i in arg:
        for j in arg1:
            list_of_values.append(z(choice, i, j))
    values = np.array(list_of_values)



def menu():
    choice1 = -1
    while choice1 != 0:
        print("\nВыберите:\n1.Task 1\n2.Task 2\n3.Task3\n4.Task4")
        while choice1 < 0 or choice1 > 4:
            choice1 = check_input("\nВаш выбор - ")
        if choice1 == 1:
            task1()
            choice1 = -1
        if choice1 == 2:
            task2()
            choice1 = -1
        if choice1 == 3:
            task3()
            choice1 = -1
        if choice1 == 4:
            task4()
            choice1 = -1


menu()