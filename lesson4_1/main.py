# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def user_info(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


print(user_info('Василий', 21, 'Москва'))
