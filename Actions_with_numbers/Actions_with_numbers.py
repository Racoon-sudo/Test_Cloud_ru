lis = list(map(int, input("Введите список чисел ").split(",")))

# Определение четных чисел
lis_2 = []
inde = 0
while inde < len(lis):
    for el in lis:
        if el % 2 == 0:
            lis_2.append(el)
        inde += 1
print("Четные числа:", lis_2)

# Определение максимального числа
print("Максимальное число:", max(lis))

# Определение минимального числа
print("Минимальное число:", min(lis))


# Сортивовка списка в порядке возрастания
lis_copy = lis.copy()

lis_empty = []

for el in range(len(lis_copy)):
    lis_empty.append(min(lis_copy))
    lis_copy.remove(min(lis_copy))

print("Отсортированный список:", lis_empty)

input()
