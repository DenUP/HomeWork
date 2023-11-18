password = "1234"
auth = input('Введите пароль: ')
while password != auth:
    print('Пароль введен не верно')
    auth = input('Попробуйте еще раз: ')
else:
    print('Пароль введен верно')
