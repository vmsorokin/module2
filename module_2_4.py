numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15]
primes = []
not_primes = []
is_prime = True
# # primes.append(numbers[2]) - добавление в список
for i in numbers[1:len(numbers)]:
    # print(i)
    for j in range(2, i):
        # print(j)
        a=i%j
        # print(f'{i}%{j}={i%j}')
        if a == 0:
            is_prime = False
            break
        else: is_prime = True
    if is_prime == True:
        primes.append(i)
    else: not_primes.append(i)
print('Простые', primes)#добовляет значение в список в зависимости от фоага
print('Составные', not_primes)
