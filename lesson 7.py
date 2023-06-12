def decimal_to_binary(decimal):
	binary = ''
	while decimal > 1:
		binary = f'{decimal % 2}' + binary
		decimal //= 2
	binary = f'{decimal}' + binary
	return binary


def is_prime(number):
	if number < 2:
		return False

	if number == 2:
		return True

	if not number % 2:
		return False

	for i in range(2, number // 2 + 1):
		if not number % i:
			return False
	return True


def generate_prime_numbers(count):
	if count < 1:
		raise ValueError('argument count must be great then 0')

	count -= 1
	yield 2
	number = 3
	while count:
		if is_prime(number):
			count -= 1
			yield number
		number += 2


def the_witcher(amount, coins=(25, 10, 5, 1)):
	coins = sorted(coins, reverse=True)
	count = 0
	for coin in coins:
		count += amount // coin
		amount -= (amount // coin) * coin
	return count


# TODO На вход функции (from_csv), поступает аргумент data в
#  качестве многострострочной строки в подобномном формате
#  привести данную строку к списку словарей
data = '''
name,age,city
vasya,23,minsk
petya,45,gomel
'''
result = [
	{'name': 'vasya', 'age': '23', 'city': 'minsk'},
	{'name': 'petya', 'age': '45', 'city': 'gomel'},
]


def to_csv(data):
	csv = ','.join(data[0].keys()) + '\n'
	return csv + '\n'.join([','.join(value.values()) for value in data])


def from_csv(data):
	data = data.strip().split('\n')
	keys = data[0].split(',')
	values = [value.split(',') for value in data[1:]]
	return [dict(zip(keys, value)) for value in values]
	return result


# TODO Написать функцию, которая принимает положительное число
#  и генерирует треугольник вида (4)
#  [[1],
#  [3, 5],
#  [7, 9, 11],
#  [13, 15, 17, 19]]


def odd_triangle(depth):
	trinagle = []
	for i in range(depth):
		line = []
		start = i*(i+1) + 1
		end = start + i * 2 + 1
		for j in range(start, end, 2):
			line.append(j)
		trinagle.append(line)
	return trinagle


def odd_triangle_2(depth):
	trinagle = []
	number = 1
	for i in range(depth):
		line = []
		for j in range(i+1):
			line.append(number)
			number += 2
		trinagle.append(line)
	return trinagle


# TODO ШИФР ВЕРНАМА
#  На вход функции подается 2 строки, ключ шифрования и сообщение
#  обязательно одинаковой длины
#  Каждый символ ключа и сообщения переводится в 2 систему счисления
#  Между соответсвующими двоичными представления по индексу
#  произвести бинарное исключительное ИЛИ
#  sms: LONDON
#  key: SYSTEM
#  01001100 01001111 01001110 01000100 01001111 01001110 SMS
#  01010011 01011001 01010011 01010100 01000101 01001101 KEY
#  00011111 00010110 00011101 00010000 00001010 00000011 RES
from typing import List, Dict, Union, Sequence


def vernama_encode(key: str, sms: str) -> Sequence[Union[str, int]]:
	return [ord(key[i]) ^ ord(sms[i]) for i in range(len(key))]


def vernama_decode(key, crypt_sms) -> str:
	return ''.join([chr(ord(key[i]) ^ crypt_sms[i]) for i in range(len(key))])


def foo(*args: int, **kwargs: str):
	pass


# TODO На вход функции подается химическая формула в виде строки
#  (в формуле только химические элементы из 1 символа и без скобок)
#  необходимо сформировать словарь с указанием колличества каждой
#  молекулы
#  C2H5OH -> {'C': 2, 'H': 6, 'O': 1}
#  CCHHHHHOH
from collections import Counter


def chemical_brothers(formula: str) -> Counter:
	if formula[-1].isalpha():
		formula += '1'
	formula = list(formula)
	formula = ''.join([
		formula[i] * int(formula[i+1])
		if formula[i+1].isdigit()
		else formula[i]
		for i in range(len(formula) - 1)
		if formula[i].isalpha()
	])
	return Counter(formula)