string = input('Введите слово ')
string = string.lower() # Переводим в нижний регистр, потому что Шалаш и шалаШ не будут равны.
if string in string[::-1]:
    print('Слово')
else:
    print('No')