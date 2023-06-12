# n = 3
# data = {i: {'name': input(f'name{i}'), 'email': input(f'email{i}')} for i in range(n)}
# print(data)


# a = 5

# if a > 0:
# 	print('a is positive')
# elif a == 0:
# 	print('a is zero')
# elif a == 5:
# 	print('a equal 5')
# else:
# 	print('a is negative')

# print('finish')

# users = []
# if users:


# a = 5
# if a > 5 == True:
# 	pass

# if not a > 5:
# 	pass

# a = int(input())

# is_even = 'No' if a % 2 else 'Zero' if a == 0 else 'Yes'

# if a % 2:
# 	is_even = 'No'
# else:
# 	is_even = 'Yes'


# x = True
# y = False
# z = False
# if not x or y:  # 0 + 0 = 0
# 	print(1)
# elif not x or not y and z:  # 0 + 1 * 0 = 0 + 0 = 0
# 	print(2)
# elif not x or y or not y and x:  # 0 + 0 + 1 * 1 = 0 + 0 + 1 = 1
# 	print(3)
# else:
# 	print(4)

# a = 'hello'


# if a.islower() or a % 2:
# 	pass

# a = 0 or 4
# print(a)
# b = 0 and 4
# print(b)

# a = True
# if isinstance(a, int | float) and not isinstance(a, bool):
# 	print('YES')
# a = 5
# if type(a) == int or type(a) == float:
# 	pass
# if isinstance(a, int | float):
# 	pass


# print(any([0, 0, 5]))


# for number in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 	number **= 2
# 	print(number)


# text = 'hello'
# for i in text:
# 	print(i)


# data = {
# 	'key1': 'value1',
# 	'key2': 'value2',
# 	'key3': 'value3'
# }

# for i, j in data.items():
# 	print(i, j)

# text = 'hello'
# print([*enumerate(text)])
# for i, j in enumerate(text, start=2):
# 	print(i, j)


# words = ['hello', 'python', 'world']

# for i in range(len(words)):
# 	print(words[i])


# numbers = [2, 3, 3, 3, 3, 4, 5, 5, 7, 6, 7]
# for i in numbers[::-1]:
# 	if i % 2:
# 		numbers.remove(i)
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# for number in numbers.copy():
# 	numbers.append(number)
# print(numbers)

# for i in range(100):
# 	# if i % 2:
# 	# 	continue

# 	if i % 2:
# 		continue

# 	print(i)
# else:
# 	print('finish')


# n = 5
# numbers = [2 ** i for i in range(1, n+1)]
# print(numbers)
# numbers = [2 ** i for i in range(1, n+1) if i % 2]
# for i in range(1, n+1):
# 	if i % 2:
# 		numbers.append(2 ** i)
# print(numbers)



# a = 0
# while a < 100:
# 	a += 1
# 	print(a)


# TODO Спрашивать данные у пользователя с клавиатуры, пока он
#  не введет число
# while not (a := input()).isdigit(): ...

# a = input('Enter number: ')
# while not a.isdigit():
# 	a = input('Are you stupid? Try again: ')


# TODO Вводится сумму вклада и процент по вкладу, сказать
#  на какой год сумма вклада удвоится (вклад капитализации)
# 100 10
# 110
# 121
# 133,1
# deposit = 100
# percent = 1 + (10 / 100)
# target = deposit * 2
# year = 0
# while deposit < target:
# 	year += 1
# 	deposit *= percent
# print(year)

# Было: numbers = ['1', '2', '3', '4', '5']
# Стало: numbers = [1, 2, 3, 4, 5]

# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(number) for number in numbers]
# for i, number in enumerate(numbers):
# 	numbers[i] = int(number)
# print(numbers)

# numbers = range(0, 11, 2)
# numbers = iter(numbers)

# for i in numbers:
# 	print(i)
# 	if i == 6:
# 		break

# for i in numbers:
# 	print(i**2)


# for i in range(10):
# 	pass

# print(i)

# TODO Дан словарь, ключами являются строки, значениями различные
#  типы данных, вывести ключи, у которых значение является
#  числом
# data = {
# 	'key1': 10,
# 	'key2': 'hello',
# 	'key3': False,
# 	'key4': [1, 2, 3],
# 	'key5': 3.14
# }
# for key, value in data.items():
# 	if isinstance(value, (int, float)) and not isinstance(value, bool):
# 		print(key)


# words = ['hello', 'world', 'python']
# for i in words:
# 	for j in i:
# 		print(j)

# try:
# 	a = int(input())
# 	b = int(input())
# 	c = a / b
# except ValueError:
# 	print('not number')
# except ZeroDivisionError:
# 	print(' zero division')
# except Exception:
# 	print('error')
# else:
# 	print('ошибок не было')
# finally:
# 	print('в любом случае')
# # EAFP


# raise ValueError('Not enough money!')
# a = input()
# if not a.isdigit():
# 	raise ValueError('invalid amount')
# N = 44
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44


# objs = [
# 	[1, 2, 3],
# 	[4, 5, 6]
# ]

# for i in objs:
# 	i.append(0)
# print(objs)

# words = ['hello', 'word']
# for word in words:
# 	word = word.upper()
# print(words)