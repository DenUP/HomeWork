stroka = 'String will never be empty and you do not need to account for different data types.'
slova = stroka.split(' ')
min_len = 999
max_len = 0
for i in slova:
    if max_len < len(i):
        max_len = len(i)
        max_slovo = i
    if min_len > len(i) and i != '':
        min_len = len(i)
        min_slovo = i
print(f"Максимальное слово: {max_slovo}, самое маленькое слово: {min_slovo}")