# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

start = int(input("Введите результат первого дня в км. : "))
end = int(input("Введите результат последнего дня в км. : "))
end += end * 0.1
day = 1
while start <= end:
    print(f'{day} день = {round(start, 2)} км.')
    start += start * 0.1
    day += 1
print(f'На {day - 1}-й день спортсмен достиг результата - не менее {round(start - start * 0.1)} км.')