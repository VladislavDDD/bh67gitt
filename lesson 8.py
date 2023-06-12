class Human:
	is_human = True

	def __init__(self, name, surname):
		self.name = name.title()
		self.surname = surname.title()
		self.city = 'Minsk'

	def __str__(self) -> str:
		return f'User: name={self.name}, surname={self.surname}'

	def __repr__(self) -> str:
		return f'User: name={self.name}, surname={self.surname}'

	@classmethod
	def from_list(cls, data: list[dict[str, str]]) -> list["Human"]:
		return [cls(**obj) for obj in data]

	@classmethod
	def foo(cls):
		pass

	@staticmethod
	def bar():
		print('bar')

	def __ge__(self, other):
		if isinstance(other, Human):
			return self.name >= other.name
		elif isinstance(other, str):
			return self.name >= other
		raise TypeError

	def __lt__(self, other):
		return not self.__ge__(other)


# data = [{'name': 'alex', 'surname': 'alexandrov'}, {'name': 'vasya', 'surname': 'pupkin'}]
# alex, vasya = Human.from_list(data)
# print(alex >= 'Alex')

# TODO Написать класс Button,
#  1. конструктор класса принимает
#  аргументы text: str, link: str, конструктор класса должен
#  объявлять атрибуты объета на основании принятых аргументов
#  2. Написать метод объекта dict, возвращающий словарь,
#  где в качестве ключей должны выступать имена аргументов в виде
#  строк, а значениями должны являться значения аргументов


class Button:

	def __init__(self, text: str, link: str) -> None:
		self.text = text
		self.link = link

	def dict(self) -> dict:
		return {'text': self.text, 'link': self.link}


# TODO Написать класс Keyboard
#  1. конструктор класса принимает name: str
#  и список экземпляров класса Button, и объявляющий атрибуты объекта
#  на основании аргументов
#  2. Написать метод объекта dict, возвращающий словарь
#  с ключами ввиде имен атрибутов в виде строк, а значения
#  значения атрибутов, при чем каждый экземпляр класса
#  Button в соответсвующей атрибуте, так же должен быть
#  приведен к словарю
#  {
# 	'name': 'Keyboard1',
# 	'buttons': [
# 		{
# 			'text': 'Button1',
# 			'link': 'http://link.1'
# 		},
# 		{
# 			'text': 'Button2',
# 			'link': 'http://link.2'
# 		}
# 	]
# }


class Keyboard:

	def __init__(self, name: str, *buttons: Button) -> None:
		self.name = name
		self.buttons = buttons
		self.i = -1

	def dict(self):
		return {
			'name': self.name,
			'buttons': [button.dict() for button in self.buttons]
		}

	def __iter__(self):
		return self

	def __next__(self):
		self.i += 1
		try:
			return self.buttons[self.i].dict()
		except IndexError:
			self.i = -1
			raise StopIteration


# buttons = [Button(f'button{i}', f'http://link.{i}') for i in range(1, 11)]
# keyboard1 = Keyboard('Keyboard 1', *buttons)
# i = iter(keyboard1)
# print(next(i))
# for button in keyboard1:
# 	print(button)
# print(Keyboard.dict(keyboard1))
# print(keyboard1.dict())



def is_palindrome(text: str) -> bool:
	"""Проверка строки на палиндроме
	:param text: Строка для проверки
	:return: True если аргумент text является палиндромом, в противном случае False
	"""
	return text.lower() == text.lower()[::-1]


# TODO Написать класс ConfigParser
#  конструктор класса принимает строковый аргумент в виде
text = ''' 
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
key5=value5
'''

#  1. Написать метод объекта dict, приводящий эту строку к словарю вида
#  {
#  	'Section1':
# 		{'key1': 'value1', 'key2': 'value2'},
#  	'Section2':
#  		{'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
# }

# 2. Написать метод объекта get приминающий имя секции и ключ и возвращающий
#  значение, если нет такой секции или ключа в указанной секции, то вызвать
#  исключение ValueError

# 3. Написать метод объекта add_section принимающий имя новой секции и создающий
#  ее, если такая секция есть, вызывать исключение ValueError

#  4. Написать метод объекта add_param приминающий имя секции,
#  имя нового ключа и его значение, и создающий
 # новый ключ со значение в указанной секции
 # в случае если нет секции - исключение
 # в случае если в секции уже есть такой параметр, изменить его значение
 # на новое