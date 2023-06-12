# # # # objs = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 1, 1, 2, 2, 2, ]
# # # # for obj in objs.copy():
# # # # 	if objs.count(obj) > 1:
# # # # 		objs.remove(obj)

# # # # print(objs)

# # # # a = [1, 2, 3]
# # # # b = [4, 5, 6]
# # # # for i in [*a, *b]:
# # # # 	print(i)


# # # # data = {
# # # # 	'key1': 'value1',
# # # # 	'key2': 'value2'
# # # # }

# # # # print(*data.items())

# # # # data1 = {'name': 'vasya', 'city': 'mogilev'}
# # # # data2 = {'city': 'minsk'}
# # # # data3 = {**data1, **data2}
# # # # data4 = data1 | data2
# # # # print(data3)

# # # # FIFO - First In First Out
# # # # LIFO - Last In First Out

# # # def is_palindrome(text):
# # # 	return text.lower() == text.lower()[::-1]


# # # def foo(a=5):
# # # 	print(a)


# # # def bar(b, a=None):
# # # 	if a is None:
# # # 		a = []
# # # 	a.append(b)
# # # 	print(a)


# # # def baz(*args):
# # # 	print(args)


# # # def kw(**kwargs):
# # # 	print(kwargs)


# # # def func(a, b, c=4, *args, d=None, **kwargs):
# # # 	print(a)
# # # 	print(b)
# # # 	print(c)
# # # 	print(d)
# # # 	print(args)
# # # 	print(kwargs)


# # # def func2():
# # # 	return 3, 4, 5


# # # def func3(a):
# # # 	a.append(1)


# # # def func4():
# # # 	a = 3
# # # 	def wrapper():
# # # 		nonlocal a
# # # 		# a = 4
# # # 		print(a)
# # # 	print(locals())
# # # 	wrapper()


# # # # print(globals()['func4'])


# # # # is_even = lambda x: x % 2 == 0
# # # # print(is_even(5))


# # # # numbers = [3, 4, '-2', -6, '-4', 5, -100]
# # # # # [3, 4, 2, 6, 4, 5, 100]
# # # # numbers.sort(key=lambda x: abs(int(x)))
# # # # print(numbers)


# # # # numbers = ['3', '5', '2', '7', '4']
# # # # result = [*map(lambda x: int(x)**2, numbers)]
# # # # result2 = [int(i)**2 for i in numbers]
# # # # print(result)

# # # # numbers = [5, -3, 5, 4, -5, -2, -6]
# # # # result = [*filter(lambda x: x > 0, numbers)]
# # # # result2 = [i for i in numbers if i > 0]
# # # # print(result)


# # # # text = 'hel'
# # # # numbers = [1, 2, 3]
# # # # objs = [None, ..., True]
# # # # # strict - python3.10+
# # # # result = [*zip(text, numbers, objs, strict=True)]
# # # # print(result)


# # # # from functools import reduce


# # # # numbers = [0, 0, 0, 4, -1, 3, 5, 2, 5, -23, -3, 0, 2]
# # # # result = reduce(lambda x, y: (abs(x) * abs(y)) if y and x else abs(x) if x else abs(y), numbers)
# # # # print(result)


# # # def foo():
# # # 	print('foo')


# # # def bar(func):
# # # 	func()


# # # bar(foo)


# # # def foo(a):
# # # 	def wrapper(b):
# # # 		return a * b

# # # 	return wrapper


# # # res = foo(4)
# # # print(res(6))
# # # print(res(5))



# # def square_range(start, stop, step):
# # 	for i in range(start, stop, step):
# # 		yield i ** 2


# # def recursive_factorial(number):
# # 	if number > 1:
# # 		number *= recursive_factorial(number - 1)
# # 	return number


# # numbers = [3, 4, 2, 3, 4, [5, 4, 5, 3, 4, [6, 5, 7, 8, 3, 4, [4, 5, 32, 4, 2], [6, 4, 5, 3, 4, ], [6, 5, 3, 4, [2, 3, 1, 2, 5, 4, 6, [8, 7, 9, 4, 5, 3, 4]]]]]]


# # def recursive_multiply(numbers):
# # 	result = 1
# # 	for number in numbers:
# # 		if isinstance(number, int | float):
# # 			result *= number
# # 		elif isinstance(number, list | tuple):
# # 			result *= recursive_multiply(number)
# # 	return result


# def is_decimal(func):
# 	def wrapper(*args):
# 		new_args = []
# 		for arg in args:
# 			if not isinstance(arg, int | float):
# 				raise TypeError
# 			else:
# 				new_args.append(arg * 2)
# 		result = func(*new_args)
# 		return f'{result=}'

# 	return wrapper

# # @is_decimal
# def multiply(*args):
# 	from functools import reduce
# 	return reduce(lambda x, y: x * y, args)


# wrapped_multiply = is_decimal(multiply)

# # print(multiply(1, 2, 3, 4, 5))


# # def is_instance(*types):
# # 	def wrapper(func):
# # 		def wrapped(*args):
# # 			if len(types) != len(args):
# # 				raise ValueError('не верное колличество типов')

# # 			for i in range(len(types)):
# # 				if not isinstance(args[i], types[i]):
# # 					raise TypeError('не верный тип')

# # 			return func(*args)

# # 		return wrapped
# # 	return wrapper


# # @is_instance(str, int)
# # def multiply_string(text, n):
# # 	return text * n


# class Dispatcher:
# 	register = []

# 	def __call__(cls):
# 		def wrapper(func):
# 			cls.register.append(func)
# 			def wrapped(*args):
# 				return func(*args)
# 			return wrapped
# 		return wrapper


# dp = Dispatcher()

# @dp()
# def foo():
# 	pass


# @dp()
# def bar():
# 	pass


# print(dp.register)


funcs = []


def dispatcher(func):
	funcs.append(func)
	def wrapper(*args):
		return func(*args)

	return wrapper


@dispatcher
def foo():
	pass


@dispatcher
def bar():
	pass


print(funcs)