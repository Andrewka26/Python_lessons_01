# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = int(input("Введите число не более 9999: "))
if num < 10:
    multiplier1 = 11
    multiplier2 = 111
elif num < 100:
    multiplier1 = 101
    multiplier2 = 10101
elif num < 1000:
    multiplier1 = 1001
    multiplier2 = 1001001
elif num < 10000:
    multiplier1 = 10001
    multiplier2 = 100010001
print(f'{num + (num * multiplier1) + (num * multiplier2)}')