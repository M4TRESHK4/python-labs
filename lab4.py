import math

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
