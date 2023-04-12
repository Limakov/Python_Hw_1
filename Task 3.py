# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
attempt = 1
print('Необходимо угадать число от 0 до 1000 за 10 попыток')

while attempt < 11:
    number_computer = randint(0, 1000)
    #print(number_computer)
    number_user = int(input('введи число \n'))
    if number_user == number_computer:
        print('В яблочко(*_*)')
        break
    else:
        attempt += 1
        print(f'не угадал, {attempt} попытка')




