# На вход программе подаются 3 целых числа
first, second, third = map(int, input("Введите три целых числа разделенных пробелом: ").split())
print('Вы ввели 3 числа: ', first, second, third)

if first == second and first == third:                      # Если все числа равны между собой
    print(3)                                                # вывести 3
elif first == second or first == third or second == third:  # Если хотя бы 2 из 3 введённых чисел равны между собой
    print(2)                                                # вывести 2
else:                                                       # Если равных чисел среди 3-х вообще нет
    print(0)                                                # вывести 0
