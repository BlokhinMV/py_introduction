# Задача 1 - Запросить число и прибавить к нему 2, вывести результат
number = int(input('Введите число'))
print(number + 2)

# Задача 2 - Используя цикл, запрашивать у пользователя число, пока оно не станет больше 0, но меньше 10
# Возвести полученное число в квадрат и вывести

while True:
    number = int(input('Введите число'))
    if number > 0 and number < 10:
        print(number ** 2)
        break
    else:
        print('Неверно! Вводимое число должно быть в диапазоне от 0 до 10')

# Задача 3 - Медицинская анкета
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))
condition = None

if age <= 30 and (weight >= 50 and weight <= 120):
    condition = 'хорошее состояние'
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    condition = 'следует заняться собой'
elif age > 40 and (weight < 50 or weight > 120):
    condition = 'следует обратиться к врачу!'
else:
    condition = 'необходимо проверить параметры через год'

print(name, surname,',', age, 'год,', 'вес', weight, '-', condition)