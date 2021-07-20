# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите число в секундах: "))
hour = time // 3600
minut = time // 60 - hour * 60
sec = time % 60
if hour <= 0:
    hour = "00"
elif hour < 10:
    hour = "0" + str(hour)
if minut <= 0:
    minut = "00"
elif minut < 10:
    minut = "0" + str(minut)
if sec <= 0:
    sec = "00"
elif sec < 10:
    sec = "0" + str(sec)
print(f'{hour}:{minut}:{sec}')