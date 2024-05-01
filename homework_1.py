# Возврат квадрата чисел
def power_numbers(*args):
      return [number*number for number in args]
print(power_numbers(1, 2, 5, 7))


#Проверка простого числа
def is_prime(num):
    n = num
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count +=1
    return f"{num}  True " if count == 2 else f"{num} False"

# Вывод четных, нечетных, просых чисел
def filter_numbers(*args):
    ODD = [
        num for num in args
        if num % 2 == 1
    ]
    print(ODD)
    EVEN = [
        num for num in args
        if num % 2 == 0
    ]
    print(EVEN)
    PRIME = [ 
        is_prime(num) for num in args
    ]
    print(PRIME)
filter_numbers(2, 1, 3, 5, 4)    
