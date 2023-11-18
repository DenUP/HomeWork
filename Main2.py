string = input('Введите слово ')
string = string.lower() # Переводим в нижний регистр, потому что Шалаш и шалаШ не будут равны.
if string == string[::-1]:
    print('Yes')
else:
    print('No')