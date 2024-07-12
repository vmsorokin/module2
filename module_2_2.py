first, second, third =map(int, input('Введите три целых числа, разделенных пробелом:  ').split())
if first==second and second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:print(0)
