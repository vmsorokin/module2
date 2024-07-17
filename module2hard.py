n = 11
n1 = int(n//2)
vs1_ = list(range(1, n1))
vs_ = list(range(1, n))
o = []
for i in vs1_:
    for j in vs_:
        if i == j:
            continue
        else:
            sum_ = i + j
            if n % sum_ == 0:
                o1 = f'{i}{j}'
                o.append(o1)
            else:
                continue

print(o)

# n = int(input('Введите число с первой вставки (от 3 до 20) '))
# if n < 3 or n>20:
#     print('Вас настигли шипы, вы не умеете читать...')
# else:
