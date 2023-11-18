password = "1234"
auth = input('Введите пароль: ')
while password != auth:
    print('Попробуй еще раз')
    auth = input('Попробуйте еще раз: ')
else:
    print('Пароль введен верно')
