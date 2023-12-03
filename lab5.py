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