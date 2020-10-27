# Создайте модуль.
# В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random

nums = [1, 2, 3, 4]


def get_random_int(numbers):
    if len(numbers) == 0:
        return None
    return random.choice(numbers)


print(get_random_int(nums))