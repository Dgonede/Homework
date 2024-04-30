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

# Четные, не четные числа
def filter_numbers(*args):
    for number in args:
      if(number % 2) == 0:
        print(f"{number} is even number")
      elif(number % 2) == 1:
        print(f"{number} is odd number")
      continue
    return args 
filter_numbers (1, 2, 5, 7)       
print(is_prime(47))


