# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = int(input("Введите количество элементов: "))
input_list = []
output_list = []
for el in range(my_list):
    input_list.append(input(f'Введите {el + 1}-й элемент: '))
for el in range(my_list // 2):
    el *= 2
    output_list.extend(reversed(input_list[el:el + 2]))
if my_list % 2:
    output_list.append(input_list[-1])
for el in range(my_list):
    print(f'Элементу {input_list[el]} = элемент {output_list[el]}')