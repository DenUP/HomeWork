def main_1():
    max=0
    n = 999
    for i in range(100, n + 1):
        a_str = str(i)
        a = int(a_str[0])
        b = int(a_str[1])
        c = int(a_str[2])
        m = i/(a+b+c)
        if max < m:
            max = m
            print(f'Максимальное значение {m} от числа {i}')

main_1()

