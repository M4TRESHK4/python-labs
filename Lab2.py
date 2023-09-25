#def CountFibonachi():
#   a = int(input("Введите число для расчета фибоначи"))
def fibonacci_sum():
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    n = int(input("Введите число: "))
    result = fibonacci_sum(n)
    print(f"Сумма чисел Фибоначчи до {n} равна {result}")


while True:
    print("\nМеню:")
    print("№1. ")
    print("№2. ")
    print("№3. ")
    print("№4. ")
    print("Выход. ")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        fibonacci_sum()
    #elif choice == '2':
#
    #elif choice == '3':
#
    #elif choice == '4':
#
    #elif choice == '5':


        break 
    else:
        print("Пожалуйста, выберите правильный пункт меню.")
    