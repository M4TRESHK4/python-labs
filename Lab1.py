#def task1():
a = int(input('введите число:'))
for i in range (1, a):
    if a%i ==0:
        print(i)
print(a)

#def task2():
str = input('введите строку:')

words = str.split(' ')
biggest_word = ''
length = len(words)

for i in range(0, length):
    if len(words[i]) > len(biggest_word):
        biggest_word = words[i]

print('кол-во слов:', length)   
print('самое длинное слово:', biggest_word) 

#def task3():
n = int(input('введите число n:'))

array = []
resultArray = []

for i in range(0, n):
    array.append(int(input(f"введите {i+1} число: ")))

for i in range(0, n-1):
    resultArray.append(array[i]+array[i+1])

print('начальный массив:')
for i in array:
    print(i, end=', ')

print('\nобработанный массив:')
for i in resultArray:
    print(i, end=', ')

#def task4():
my_dict = {'b': 3, 'a': 5, 'd': 1, 'c': 7}

print('\nотсортированный словарь по возрастанию:')
print('\n',dict(sorted(my_dict.items())))
print('отсортированный словарь по убыванию:')
print('\n',dict(sorted(my_dict.items(), reverse = True)))

max_value_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_value_key]
print(f"\nЭлемент с максимальным значением: {max_value_key}: {max_value}")

#def task5():



#def task6():

cort = (1, 2, 3, 4, 5)

sorted = tuple(sorted(cort, reverse = True))
max = 0
min = 0
for i in range(0, len(sorted)):
    if sorted[i] > max:
        max = sorted[i]
    if sorted[i]< max:
        min = sorted[i]

print(sorted)
print(f"max value: {max}")
print(f"min value: {min}")

#def showMenu():
#    while(True):
#        print("""\nМеню:
#        1. Задание 1
#        2. Задание 2
#        3. Задание 3
#        4. Задание 4
#        5. Задание 5
#        6. Задание 6
#        0. Выход""")
#
#        choice = input("Выберите пункт меню: ")
#
#        if(choice == "1"):
#            task1()
#
#        elif(choice == "2"):
#            task2()
#
#        elif(choice == "3"):
#            task3()
#
#        elif(choice == "4"):
#            task4()
#
#        elif(choice == "5"):
#            task5()
#
#        elif(choice == "6"):
#            task6()
#
#        elif(choice == "0"):
#            print("До свидания!")
#            break
#
