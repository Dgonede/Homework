# Возврат квадрата чисел
def power_numbers(*args):
      return [number*number for number in args]


# Нечетные числа
num = []
def odds(*args):
    for num in args:
        if num % 2 == 1: return True
        if num % 2 == 0: return False
ODD = odds

# Четные числа
nums = []
def evens(*args):
    for evens in args:
        if evens % 2 == 1: return False
        if evens % 2 == 0: return True
EVEN = evens

def prime(num):
    if num == 1:return False
    nums = True
    i = num - 1
    while i > 1:
        if not num % i:
            nums = False
            break
        i -= 1
    return num if nums else False

PRIME = prime

def filter_numbers(a,b):
    return list(filter(b,a))
print(power_numbers(1, 2, 5, 7))
print(filter_numbers([1, 2, 3], ODD)) 
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([47,49, 54, 2, 5], PRIME))
