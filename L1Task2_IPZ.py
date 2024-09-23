# Програма для розрахунку чисел Фібоначчі

def fibonacci(n):
    fib_sequence = [0, 1]  # Перші два числа Фібоначчі
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

# Користувач вводить кількість чисел Фібоначчі
n = int(input("Введіть кількість чисел Фібоначчі: "))

# Викликаємо функцію та виводимо результат
fib_sequence = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {fib_sequence}")
