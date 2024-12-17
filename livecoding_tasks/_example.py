from datetime import datetime
def factorial(n):
    total = 1
    for i in range(1, n+1):
        total += i
        print(total, end=" ")

# Пример использования
start = datetime.now()
factorial(1000000)
end = datetime.now()
total_time = end - start
print(f"\n{total_time}")