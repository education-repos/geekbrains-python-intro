# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
# имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

# (Формула не соответствует реальной действительности и здесь используется только ради примера)
# Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.
# Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно.
# В случае ошибок, уточните условия для той или иной ситуации.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

result = ''
first_name = input('enter first name ')
last_name = input('enter last name ')
name = first_name + ' ' + last_name
age = int(input('enter age '))
age_full = str(age) + ' год'
weight = int(input('enter weight '))
weight_ful = 'вес ' + str(weight)
if age <= 30 and 120 >= weight >= 50:
    result = 'хорошее состояние'
elif weight > 120 or weight < 50:
    if age > 40:
        result = 'следует обратится к врачу!'
    elif age > 30:
        result = 'следует заняться собой'
else:
    result = 'wtf'
print(name, age_full, weight_ful, result, sep=', ')
