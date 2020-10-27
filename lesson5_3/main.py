# Создайте модуль main.py.
# Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.
from .lesson51 import make_dirs, remove_dirs
from .lesson52 import get_random_int

make_dirs()
print(get_random_int([1, 2, 3]))
remove_dirs()