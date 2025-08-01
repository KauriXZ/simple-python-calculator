def calc(x,y):
  if choose == '1':
    z = x + y
  elif choose == '2': 
    z = x - y
  elif choose == '3':
    z = x * y
  elif choose == '4':
    if y != 0:
      z = x / y
    else:  
      z = print('Делить на ноль нельзя! ')
  return z
   



print('Добро пожаловать в калькулятор!')
print('1 - сложение 2 - вычитание 3 - умножение 4 - деление 0 - выход')
while True: 
  choose = input('Выберите нужную вам операцию: ')
  if choose != '0':
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число '))
    z = calc(x,y)
    print(f'Ваш ответ: {z}')
  else:
    print('До скорых встреч!')
    input('Нажмите Enter, чтобы выйти...')
    break