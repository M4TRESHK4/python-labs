import math
import time


class Circle:
    radius = 12

    def squre():
        square = math.pi*pow(Circle.radius, 2)
        if (Circle.radius < 0):
            print('Радиус меньше нуля, посчитать площадь не получится!!!!!!!!')
        else:
            print(square) 

    def length():
        length = 2*math.pi*Circle.radius
        if (Circle.radius < 0):
            print('Радиус меньше нуля, посчитать длину окружности не получится!!!!!!!!')
        else:
            print(length)

Circle.squre()
Circle.length()

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("Red light. Stop!")
                time.sleep(7)
                self.__color = "yellow"

            elif self.__color == "yellow":
                print("Yellow light. Get ready!")
                time.sleep(2)
                self.__color = "green"

            elif self.__color == "green":
                print("Green light. Go!")
                time.sleep(5)
                self.__color = "red"

traffic_light = TrafficLight()
traffic_light.running()