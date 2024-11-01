import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі дійсні числа, відокремлені пробілами, за допомогою регулярного виразу
    for match in re.finditer(r'\b\d+\.\d+\b|\b\d+\b', text):
        yield float(match.group())  # Повертаємо числа як float для обчислення

def sum_profit(text: str, func: Callable) -> float:
    # Використовуємо генератор для підсумовування чисел у тексті
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")  # Округлення до двох десяткових знаків для коректного виводу