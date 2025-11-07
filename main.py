import random

def tsikly() :
    print("Раздел: Циклы")

    # 1. Вывести таблицу умножения от 1 до 9 с табуляцией.
    print("Таблица умножения 1-9:")
    for i in range(1, 10) :
        for j in range(1, 10) :
            print(f"{i} * {j} = {i * j}\t", end="")
        print()

    # 2. Сумма всех нечётных чисел от 1 до 100.
    summa = 0
    for i in range(1, 101, 2) :
        summa += i
    print("Сумма нечётных от 1 до 100:", summa)

    # 3. Запросить n и вывести делители.
    n = int(input("Введите n для делителей: "))
    print("Делители:", end=" ")
    for i in range(1, n + 1) :
        if n % i == 0 :
            print(i, end=" ")
    print()

    # 4. Факториал числа.
    n = int(input("Введите число для факториала: "))
    fact = 1
    for i in range(1, n + 1) :
        fact *= i
    print("Факториал:", fact)

    # 5. Последовательность Фибоначчи длиной n.
    n = int(input("Введите длину Фибоначчи: "))
    fib = [0, 1]
    for i in range(2, n) :
        fib.append(fib[-1] + fib[-2])
    print("Числа Фибоначчи:", fib[:n])


def spiski() :
    print("Раздел: Списки")

    # 0. Генерация списка случайных чисел.
    numbers = [random.randint(-50, 50) for _ in range(10)]
    print("Сгенерированный список:", numbers)

    # 1. Только чётные элементы.
    even = [x for x in numbers if x % 2 == 0]
    print("Чётные:", even)

    # 2. Макс и мин в списке.
    print("Макс:", max(numbers), "Мин:", min(numbers))

    # 3. 5 чисел от пользователя, добавление в numbers и сортировка.
    for _ in range(5) :
        numbers.append(int(input("Введите число: ")))
    numbers.sort()
    print("Объединённый и отсортированный список:", numbers)

    # 4. Удалить дубликаты без set.
    unique = []
    for x in numbers :
        if x not in unique :
            unique.append(x)
    print("Без дубликатов:", unique)

    # 5. Поменять первый и последний.
    if len(numbers) >= 2 :
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
    print("После обмена:", numbers)


def slovari() :
    print("Раздел: Словари")

    # 1. Словарь студентов и оценок, средний балл.
    students = {"Настя Симоненко" : 5, "Дарья Зацепина" : 4, "Лиза Михайлова" : 3}
    avg = sum(students.values()) / len(students)
    print("Средний балл:", avg)

    # 2. Количество букв в строке от input.
    s = input("Введите строку: ")
    count = {}
    for char in s :
        if char.isalpha() :
            if char in count :
                count[char] += 1
            else :
                count[char] = 1
    print("Количество букв:", count)

    # 3. Ключи 1-10, значения - квадраты.
    squares = {i : i ** 2 for i in range(1, 11)}
    print("Квадраты:", squares)

    # 4. Словарь из двух списков.
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    d = {}
    for i in range(len(keys)) :
        d[keys[i]] = values[i]
    print("Из списков:", d)


def mnozhestva() :
    print("Раздел: Множества")

    # 1. Два множества, пересечение и объединение.
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Пересечение:", set1 & set2)
    print("Объединение:", set1 | set2)

    # 2. Уникальные слова в тексте от пользователя.
    text = input("Введите текст: ")
    words = set(word.strip(".,!?()[]{};:\"'") for word in text.split())
    print("Уникальные слова:", words)

    # 3. Общие элементы двух списков с set.
    lst1 = [1, 2, 3, 4]
    lst2 = [3, 4, 5, 6]
    common = set(lst1) & set(lst2)
    print("Общие:", common)

    # 4. Подмножество.
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print("A подмножество B:", set_a.issubset(set_b))

    # 5. Удалить меньше заданного числа.
    s = {10, 20, 30, 40}
    limit = 25
    s = {x for x in s if x >= limit}
    print("После удаления <25:", s)


def kombinirovannye() :
    print("Раздел: Комбинированные задания")

    # 1. Список 20 случайных чисел, выводим уникальные.
    lst = [random.randint(1, 10) for _ in range(20)]
    count = {}
    for num in lst :
        count[num] = count.get(num, 0) + 1
    unique = [num for num in lst if count[num] == 1]
    print(lst)
    print("Уникальные:", unique)

    # 2. Словарь: ключи-элементы списка, значения-колво их повторений.
    count = {}
    for x in lst :
        count[x] = count.get(x, 0) + 1
    print("Повторения:", count)

    # 3. Множество слов, длина больше 5 символов.
    words = ["яблоки", "диван", "машина", "кот"]
    long = {w for w in words if len(w) > 5}
    print("Слова >5:", long)

    # 4. Словарь вхождений слов в предложении.
    sentence = input("Введите предложение: ")
    word_count = {}
    for w in sentence.split() :
        word_count[w] = word_count.get(w, 0) + 1
    print("Вхождения слов:", word_count)

    # 5. Список, множество, список (убрать дубли).
    lst_dup = [1, 2, 2, 3]
    unique_lst = list(set(lst_dup))
    print("Список без дубликатов:", unique_lst)

    # 6. Словарь товар-цена, ищем самый дорогой.
    goods = {"яблоки" : 30, "апельсины" : 50, "вишня" : 75}
    max_good = max(goods, key=goods.get)
    print("Самый дорогой:", max_good)

    # 7. Список имён, больше 1 раза, самое частое.
    names = ["Настя", "Даша", "Лиза", "Настя", "Саша", "Ваня", "Настя", "Саша"]
    count = {}
    for n in names :
        count[n] = count.get(n, 0) + 1
    repeated = {k : v for k, v in count.items() if v > 1}
    most = max(count, key=count.get)
    print("Повторяющиеся:", repeated, "Самое частое:", most)

    # 8. Строка -> словарь символ -> первый индекс.
    s = input("Введите строку: ")
    first_index = {}
    for i, char in enumerate(s) :
        if char not in first_index :
            first_index[char] = i
    print("Первый индекс:", first_index)


while True :
    print("\nМеню разделов: 1-Циклы, 2-Списки, 3-Словари, 4-Множества, 5-Комбинированные, 0-Выход")
    choice = int(input())
    if choice == 0 :
        break
    elif choice == 1 :
        tsikly()
    elif choice == 2 :
        spiski()
    elif choice == 3 :
        slovari()
    elif choice == 4 :
        mnozhestva()
    elif choice == 5 :
        kombinirovannye()
    else :
        print("Неверный выбор")
