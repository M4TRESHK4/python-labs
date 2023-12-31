def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    
    while a <= n:
        total += a
        a, b = b, a + b
        
    return total


def whatArg(x):
    t = type(x)
    if(t is tuple):
        print('длина всех букв кортежа: ')
        print(sum([len(word) for word in x]))
               
    if(t is list):
        letter_count =0
        digit_count =0
        for item in x:
            for symbol in item:
                if(str(symbol).isdigit()):
                    digit_count += 1

                elif(str(symbol).isalpha()):
                    letter_count += 1
        print('Количество букв: ', letter_count)
        print('Количество чисел: ', digit_count)

    if(t is str):
        letter_count = 0
        for item in x:
            if(str(item).isalpha()):
                letter_count += 1
        print('Букв в строке', letter_count)

def matrix():
    matrix = [[1, -1, 1],
             [1, -2, 1],
             [-1, 2, 1]]
    print('Начальная матрица:')
    for row in matrix:
            print(row)
    has_positive_element = False

    # Проходим по каждой строке матрицы
    for row in matrix:
        for element in row:
            if element > 0:
                has_positive_element = True
                break  # Если есть положительный элемент, выходим из цикла


        if has_positive_element:
            for i in range(len(row)):
                row[i] = -row[i]

        # Сбрасываем флаг для следующей строки
        has_positive_element = False

    print('преобразованная матрица:')
    for row in matrix:
        print(row) 

def tryExcept():
    try:
        numerator = 10
        denominator = 0
        result = numerator / denominator
    except ZeroDivisionError:
        print(f"Произошло деление на ноль!")
    finally:
        print("блок finally работает всегда")

        

while True:
    print("\nМеню:")
    print("№1. ")
    print("№2. ")
    print("№3. ")
    print("№4. ")
    print("Выход. ")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
       n = int(input("Введите число: "))
       result = fibonacci_sum(n)
       print(f"Сумма чисел Фибоначчи до {n} равна {result}")
    elif choice == '2':
        whatArg(("e", "e", "r"))
        whatArg(['qwerty', '12', '233'])
        whatArg('asdfghjkl')
    elif choice == '3':
        matrix()
    elif choice == '4':
        tryExcept()
        break 
    else:
        print("Пожалуйста, выберите правильный пункт меню.")
    