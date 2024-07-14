# my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# number = 0
# while number < len(my_list):
#     a = my_list[number]
#     if a == 0:
#         number = number + 1
#         continue
#     else:
#         if a > 0:
#             print(a)
#             number = number + 1
#             continue
#         else:
#             break
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < len(my_list):
    a=my_list[number]
    if a != 0:
        if a > 0:
            print(a)
            number = number + 1
            continue
        else:
            break
    else: number = number + 1
    continue
