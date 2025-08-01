def calc(x,y,choose):
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
      z = 'Делить на ноль нельзя! Попробуйте ещё раз.'
  return str(z)
   


print('Добро пожаловать в калькулятор!')
print('1 - сложение 2 - вычитание 3 - умножение 4 - деление 0 - выход 00 - посмотреть предыдущие вычисления')
while True: 
  
  #Выбор операции
  choose = input('Выберите нужную вам операцию: ')
  

  #Проведение вычислений и добавление их в историю
  if choose != '0' and choose != '00':
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число '))
    z = calc(x,y,choose)
    print(f'Ваш ответ: {z}')
    with open('last_res.txt', 'w', encoding='utf-8') as file:
      file.write(z)
  
  
  #Просмотр результатов
  elif choose == '00':
    with open('last_res.txt', 'r', encoding='utf-8') as file:
      last_results = file.read()
      print(last_results)
  

  #Завершение работы
  else:
    print('До скорых встреч!')
    input('Нажмите Enter, чтобы выйти...')
    break