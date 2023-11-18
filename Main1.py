def main_1():
    max=0
    for i in range(100,999+1):
        a_str =str(i)
        a = int(a_str[0])
        b = int(a_str[1])
        c = int(a_str[2])
        m = i/(a+b+c)
        if max < m:
            max = m
            s = i
    print(f'Максимальное значение {max} от числа {s}')

main_1()