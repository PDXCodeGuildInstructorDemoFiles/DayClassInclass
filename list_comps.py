# names = ['David', 'Helen', 'Anne']
# lower_names = [i.lower() for i in names]
# print(lower_names)  # > ['david', 'helen', 'anne']
#
# lower_names_2 = []
#
# for n in names:
#     lower_names_2.append(n.lower())
#
# print(lower_names_2)


# print([num for num in range(101) if num % 2 == 0])


# def gen_odd_num(less_than):
#     for x in range(less_than):
#         if x % 2 == 1:
#             yield x
#
# for i in gen_odd_num(101):
#     print(i)

lst = [[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]

for x in lst:
    for i in x:
        for z in i:
            print(z)
#
# if x:
#     if z:
#         if c:



