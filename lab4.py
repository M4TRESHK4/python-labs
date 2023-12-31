import math
import time


class Circle:
    radius = 12

    def squre():
        square = math.pi*pow(Circle.radius, 2)
        if (Circle.radius < 0):
            print('Радиус меньше нуля, посчитать площадь не получится!!!!!!!!')
        else:
            print('square is', square) 

    def length():
        length = 2*math.pi*Circle.radius
        if (Circle.radius < 0):
            print('Радиус меньше нуля, посчитать длину окружности не получится!!!!!!!!')
        else:
            print('length is',length)

Circle.squre()
Circle.length()

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        i=0
        while i<4:
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
            i=i+1

traffic_light = TrafficLight()
traffic_light.running()

class TransportVehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def transportation_time(self, distance):
        pass

    def transportation_cost(self, distance):
        pass


class Airplane(TransportVehicle):
    def move(self):
        return "Flying"

    def transportation_time(self, distance):
        # Предположим, что самолет летает со средней скоростью 800 км/ч
        return distance / 800

    def transportation_cost(self, distance):
        # Предположим, что стоимость перевозки на самолете составляет 10 рублей за 1 км
        return distance * 10


class Train(TransportVehicle):
    def move(self):
        return "Traveling by train"

    def transportation_time(self, distance):
        # Предположим, что поезд движется со средней скоростью 120 км/ч
        return distance / 120

    def transportation_cost(self, distance):
        # Предположим, что стоимость перевозки на поезде составляет 5 рублей за 1 км
        return distance * 5


class Car(TransportVehicle):
    def move(self):
        return "Driving a car"

    def transportation_time(self, distance):
        # Предположим, что автомобиль движется со средней скоростью 60 км/ч
        return distance / 60

    def transportation_cost(self, distance):
        # Предположим, что стоимость перевозки на автомобиле составляет 7 рублей за 1 км
        return distance * 7


# Функция для определения наиболее быстрой и экономичной поездки
def find_optimal_transportation(distance):
    vehicles = [Airplane("Boeing"), Train("Express"), Car("Toyota")]

    fastest_vehicle = min(vehicles, key=lambda x: x.transportation_time(distance))
    cheapest_vehicle = min(vehicles, key=lambda x: x.transportation_cost(distance))

    return fastest_vehicle, cheapest_vehicle


# Функция для записи информации в файл
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')


if __name__ == "__main__":
    distance = 500

    fastest, cheapest = find_optimal_transportation(distance)

    print(f"The fastest transportation: {fastest.move()}. Time: {fastest.transportation_time(distance)} hours.")
    print(f"The cheapest transportation: {cheapest.move()}. Cost: {cheapest.transportation_cost(distance)} rubles.")

    data_to_write = [
        f"The fastest transportation: {fastest.move()}. Time: {fastest.transportation_time(distance)} hours.",
        f"The cheapest transportation: {cheapest.move()}. Cost: {cheapest.transportation_cost(distance)} rubles."
    ]
    write_to_file("transportation_info.txt", data_to_write)

class Book:
    # Метод класса для создания экземпляра книги из строки
    @classmethod
    def from_string(cls, book_string):
        title, author, year = book_string.split(',')
        return cls(title.strip(), author.strip(), int(year.strip()))

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Метод экземпляра класса для вывода информации о книге
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    # Статический метод для проверки, является ли год выпуска книги високосным
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Метод экземпляра класса для проверки, является ли год выпуска книги високосным
    def is_leap_year_instance(self):
        return self.is_leap_year(self.year)


# Создаем экземпляр книги с использованием метода класса
book_str = "The Great Gatsby, F. Scott Fitzgerald, 1925"
book1 = Book.from_string(book_str)

# Выводим информацию о книге
book1.display_info()

# Проверяем, является ли год выпуска книги високосным с использованием метода экземпляра
print(f"Is leap year: {book1.is_leap_year_instance()}")

# Используем статический метод для проверки високосного года
year_to_check = 2024
print(f"Is {year_to_check} a leap year? {Book.is_leap_year(year_to_check)}")

