# Задание 1: List comprehension
squares = [x**2 for x in range(1, 11)]
print("1. Квадраты от 1 до 10:", squares)

# Задание 2: List comprehension
evens = [x for x in range(20) if x % 2 == 0]
print("2. Чётные из range(20):", evens)

# Задание 3: List comprehension (работа со строками)
words = ["python", "Java", "c++", "Rust", "go"]
long_words = [w.upper() for w in words if len(w) > 3]
print("3. Слова длиной >3:", long_words)

