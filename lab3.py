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

# Задание 4: Класс-генератор Countdown
class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = self.n
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

print("4. Countdown от 5:")
for x in Countdown(5):
    print(x)

# Задание 5: Класс-генератор Fibonacci
class Fibonacci :
    def __init__(self, n) :
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.count >= self.n :
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result


print("5. Fibonacci(5):")
for num in Fibonacci(5) :
    print(num, end=' ')
print()


# Задание 6: Decimal
from decimal import Decimal

P = Decimal(input("P: "))
r = Decimal(input("r (%): "))
t = int(input("t (лет): "))

S = P * (1 + r / (12 * 100)) ** (12 * t)
profit = S - P   # Прибыль

print(f"Итоговая сумма: {S:.2f}")
print(f"Общая прибыль: {profit:.2f}")


# Задание 7: Fraction
from fractions import Fraction

a = Fraction(3, 4)
b = Fraction(5, 6)

print("7. Операции с дробями:")
print(f"   Сложение: {a + b}")
print(f"   Вычитание: {a - b}")
print(f"   Умножение: {a * b}")
print(f"   Деление: {a / b}")


