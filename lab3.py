def task1():

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

def task2():

    with open("testTask2.txt", 'a'):
        pass

    with open('testTask2.txt', 'r') as testTxt:
        lines = testTxt.readlines()

    import codecs #это чтоб русские символы выводились

    translator_dict = { # можешь добавлять сколько угодно цифр и преводов
        "1" : "Один",
        "2" : "Два",
        "3" : "Три",
        "4" : "Четыре"
    }
    with codecs.open("testTask2Result.txt", 'w', 'utf-8') as f: #это чтоб русские символы выводились

        for line in lines:

            line_data = line.split()

            f.write(translator_dict[line_data[2]] + ' ' + " ".join(line_data[1:]) + u'\n') # тут буква u для того же
            
def task3():

    subjects ={}

    with open("task3.txt", 'a'):
        pass

    with open("task3.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:
        subject_info = line.split(':')  
        subject_name = subject_info[0]
        subjects[subject_name] = [int(subject_info[1]), int(subject_info[2]), int(subject_info[3]), 0]
        subjects[subject_name][3] = sum(subjects[subject_name])

    for k, v in subjects.items():
        print(f"Предмет: {k}, Лекций: {v[0]}, Практических: {v[1]}, Лабораторных: {v[2]}, Всего - {v[3]}")
task1()
task2()
task3()
    
