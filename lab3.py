with open('F1.txt', 'w') as f1:
    while True:
        data = input("Введите данные(пустая строка для завершения ввода)")
        if not data:
            break
        f1.write(data+'\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
    if len(lines)>=4:
        f2.writelines(lines[3:])

with open('F2.txt', 'r') as f2:
    first_line = f2.readline()
    words = first_line.split()
    word_count = len(words)
    
print(f"Количество слов в первой строке файла F2: {word_count}")