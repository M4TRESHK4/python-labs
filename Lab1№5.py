menu = {
    'торт': ['Вкусный торт', 200, 1000],
    'пирожное': ['Нежное пирожное', 150, 1000],
    'маффин': ['Ароматный маффин', 100, 1000],
    'печенье': ['Хрустящее печенье', 50, 1000],
    'эклер': ['Нежный эклер', 180, 1000],
    'кекс': ['Пышный кекс', 120, 1000]
}
cart = {}

# Функция для вывода описания продукции
def viewProductDescription():
    for product, description in menu.items():
        print(f'{product} - {description[0]}')

# Функция для вывода цен продукции
def viewProductPrice():
    for product, description in menu.items():
        print(f'{product} - {description[1]} руб. за 100 грамм')

# Функция для вывода количества продукции
def viewProductInStock():
    for product, description in menu.items():
        print(f'{product} - {description[2]} грамм')

# Функция для вывода всей информации
def viewAllInfo():
    for product, description in menu.items():
        print(f'product: {product}')
        print(f'description: {description[0]}')
        print(f'price: {description[1]} руб. за 100 грамм')
        print(f'Количество: {description[2]} грамм')
        print()

# Функция для выполнения покупки
def purchase():
    purchaseAmount = 0

    while True:
        product = input("Введите название продукции (или '0' для выхода): ").lower()
        if product == '0':
            break
        if product in menu:
            gramms = int(input(f"Введите количество грамм {product}: "))
            if gramms<0:
                print("Введено неверное кол-во грамм")
                return
            if gramms <= menu[product][2]:
                price = (menu[product][1] / 100) * gramms
                purchaseAmount += price
                menu[product][2] -= gramms
                print(f"Вы купили {gramms} грамм {product} за {price} руб.")

                cart[product] = [price, gramms]

            else:
                print(f"Извините, недостаточно {product} в наличии.")
        else:
            print("Продукция не найдена в меню.")
    
    print(f"Сумма вашей покупки: {purchaseAmount} руб.")
    print("Обновленное количество продукции:")
    viewProductInStock()

def myCart():
    print("\nМоя корзина:\n")

    if len(cart) == 0:
        print("Корзина пуста")
    else:
        for product, description in cart.items():
            print(f'товар: {product}')
            print(f'цена: {description[0]} руб.')
            print(f'Количество: {description[1]} грамм')
            print()

    #print(f"Продукты в корзине:\n{cart}")
    
    

# Главное меню
while True:
    print("\nМеню:")
    print("1. Просмотр описания продукции")
    print("2. Просмотр цен продукции")
    print("3. Просмотр количества продукции")
    print("4. Всю информацию")
    print("5. Покупка")
    print("6. Корзина")
    print("7. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        viewProductDescription()
    elif choice == '2':
        viewProductPrice()
    elif choice == '3':
        viewProductInStock()
    elif choice == '4':
        viewAllInfo()
    elif choice == '5':
        purchase()
    elif choice == '6':
        myCart() 
    elif choice == '7':
        break 
    else:
        print("Пожалуйста, выберите правильный пункт меню.")
