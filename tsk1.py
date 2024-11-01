def caching_fibonacci():
    
    cache = {}

    # Функція, що обчислює числа Фібоначчі з кешуванням
    def fibonacci(n):
        # Базові випадки для послідовності Фібоначчі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Якщо значення вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]
        
        # Рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Повертаємо внутрішню функцію для використання

# Приклад використання:
fib = caching_fibonacci()

# Використовуємо функцію для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15))  
print(fib(50)) 