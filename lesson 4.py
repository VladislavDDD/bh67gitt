# numbers = [2, 3, 4, 5, 4, 7, 8, 5, 6, 9,]
# print(numbers[1])
# numbers[1] = 4
# print(numbers[1])
#
#
# objs = list('hello world')
# print(objs)
#
#
# objs = ['hello', 4, 5, 'world', True]
# del objs[1]
# print(objs)
#
# objs = ['hello', 4, 5, 'world', True]
# del objs[1:3]
# print(objs)
#
# objs = ['hello', 4, 5, 'world', True]
# obj = objs.pop(1)
# print(objs)
# print(obj)
#
# objs = ['hello', 4, 4, 4, 4, 4, 5, 'world', True]
# objs.remove(4)
# print(objs)
#
#
# objs = ['hello', 4, 4, 4, 4, 4, 5, 'world', True]
# objs.append([1, 2, 3])
# print(objs)
#
# objs = ['hello', 4, 4, 4, 4, 4, 5, 'world', True]
# objs.extend('hello')
# objs.extend([1, 2, 3, 4])
# print(objs)
#
#
# objs = ['hello', 4, 4, 4, 4, 4, 5, 'world', True]
# result = objs + [1, 2, 3, 4]
# print(objs)
# print(objs * 2)
# print(result)
#
#
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.insert(2, 'hello')
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# numbers.insert(0 ,0)
# print(numbers)
#
#
# numbers = [4, 6, 5, 7, 3, 8, 2, 9]
# numbers.sort()
# print(numbers)
#
# numbers = [4, 6, 5, 7, 3, 8, 2, 9]
# numbers.sort(reverse=True)
# print(numbers)
#
# words = ['hello', 'world', 'age', 'apple', 'Beautiful']
# words.sort()
# print(words)
#
# words = ['hello', 'world', 'age', 'apple', 'Beautiful']
# words.sort(key=len)
# print(words)
#
#
# numbers = [4, 6, 5, 7, 3, 8, 2, 9]
# result = sorted(numbers)
# print(numbers)
# print(result)
#
#
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = number[::-1]
# print(number)
# print(result)
#
#
# numbers = [1, 2, 3]
# result = list(numbers)
# numbers.append(4)
# print(result)
#
# numbers = [1, 2, 3]
# result = numbers.copy()
# numbers.append(4)
# print(result)
#
# numbers = [1, 2, 3]
# result = numbers[:]
# numbers.append(4)
# print(result)
#
# print(numbers[0] is result[0])
#
#
# a = [1, 2, 3]
# b = [3, 4, 5]
# b.append(a)
# a.append(0)
# print(b)
#
# a = [1, 2, 3]
# b = [3, 4, 5]
# c = b.copy()
# b.append(a)
# a.append(0)
# print(b)
#
# a = [1, 2, 'hello']
# b = [3, 4, 5]
# b.append(a)
# print(b[3] [2])
#
# a = [1, 2, 'hello']
# b = [3, 4, 5]
# b.append(a)
# b[3].append(54)
# print(a)
#
# a = [1, 2, 'hello']
# b = [3, 4, 5]
# b.append(a)
# b[3] [2] = 3
# print(a)
#
#
# numbers = [i**2 for i in range(1, 101)]
# print(numbers)

# numbers = [0 for i in range(100)]
# print(numbers)
#
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# number = [number [i]*5 for i in range(len(number))]
# print(number)
#
# text = 'hello'
# letters = list(text)
# letters[1] = 'p'
# print(letters)
#
# numbers = [1, 2, 3, 4]
# numbers[1:3] = [1, 2, 3, 4]
# print(numbers)
#
# numbers = [1, 2, 3, 4]
# a, b, c, d = numbers
# print(a)
# print(b)
# print(c)
# print(d)

# numbers = [1, 2, 3, 4]
# a, b, *c = numbers
# print(a)
# print(b)
# print(c)
#
# a = [1, 2, 3]
# b = [4, 5, 6, 7, 8, 9]
# c = 'hello'
# d = [*a, *b, *c]
# print(d)
#
# a = (4, )
# print(a)
#
# a = (1, 2, 3, 4, 9, [5, 6, 7])
# a[5].append(8)
# print(a)
#
#
# user = {
#     'name': 'Vasya',
#     'age': 23,
#     'languages': ['ru', 'en']
# }
# print(user['name'])
# user['name'] = 'Petya'
# user['city'] = 'Minsk'
# print(len(user))
#
# user = {
#     'name': 'Vasya',
#     'age': 23,
#     'languages': ['ru', 'en']
# }
# print(user['name'])
# user['name'] = 'Petya'
# user['city'] = 'Minsk'
# print(user)
#
# user = {
#     'name': 'Vasya',
#     'age': 23,
#     'languages': ['ru', 'en']
# }
# print(user['name'])
# user['name'] = 'Petya'
# user['city'] = 'Minsk'
# print('name' in user)
#
# user = dict([('name', 'Vasya'), ('age', 23)])
# print(user)
#
# data = dict(['ab', 'cd'])
# print(data)
#
# data = {i: i**2 for i in range(10)}
# print(data)
#
# data = dict.fromkeys(('name', 'age', 'city'))
# print(data)
#
# data = dict.fromkeys(('name', 'age', 'city'), 'H/Y')
# print(data)

user = {
    'name': 'Vasya',
    'age': 23,
    'languages': ['ru', 'en']
}