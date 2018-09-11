# import random
# lst = ["one", "two", "three", "four", "five"]
#
# for index, value in enumerate(lst):
#     print("{} :: {}".format(index, value))

# str = "Hello World!"
# print(str.rjust(50, ' '))
# # print(str)
# print('-' * 50)
# x = map(lambda e: (e + ' ')* 2, ['one', 'two', 'three', 'four'])
# print(list(x))

# i = 0
# test = 8
# while i <= test:
#     i += 1
#     if i >= 5 and i <= 6:
#         continue
#     elif i == 8:
#         break
#     print(i)
# else:
#     print("exited with interruption :)")

#
# collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
# print(collection)
# col1 = collection[0]
# col2 = collection[1]
# col3 = collection[2]
# print(col1)
# print(col2)
# print(col3)
#
# for col1, col2, col3 in collection:
#     print("{}\t{}\t{}".format(col1, col2, col3))


# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
# for s in lst:
#     print(s[:2])
#
# print('-' * 40)
#
# for idx, s in enumerate(lst):
#     print("%s has an index of %d" % (s[:2], idx))

# options = {"x": ["a", "b"], "y": [10, 20, 30]}

# import itertools
# options = {"x": ["a", "b"], "y": [10, 20, 30]}
# keys = options.keys()
# values = (options[key] for key in keys)
# combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
# print(combinations)

# a = [1, 2, 3, 4, 5, 6, 7, 7]
# b = [8, 9]
# str = "Hello"
# print(a)
# # a.append(b)
# a.extend(b)
# a.extend(str)
# print(a)

# import collections
# name = "Shrinivas Rao K. Gowde"
# print(name)
# name_dict = collections.defaultdict()
# for key in name:
#     if key in name_dict:
#         name_dict[key] += 1
#     else:
#         name_dict[key] = 1
# for key in name_dict:
#     print("{}: {}".format(key, name_dict[key]))


# import collections
# name = "Shrinivas Rao K. Gowde"
# print(name)
#
# name_dict = collections.defaultdict()
# for key in name.upper():
#     if key not in name_dict and key.isalpha():
#         name_dict[key] = (name.upper()).count(key)
# print(sorted(name_dict.items()))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst = list(range(1, 10))
# print(lst)
# for (index, item) in enumerate(lst, start=1):
#     print("{}: {}".format(index, item))

# lst = list(range(1, 11))
# print(lst)
# for i in lst:
#     if i == 1:
#         del lst[i]
#     print(i)
# print(lst)

# lst = [i for i in range(1, 11)]
# print("lst: {}".format(lst))
# print("Reversed lst: {}".format(list(reversed(lst))))
# print("sliced lst: {}".format(lst[::-1]))

# for i in range(0, 10):
#     for j in range(0,i):
#         print('*', end='')
#     print()

