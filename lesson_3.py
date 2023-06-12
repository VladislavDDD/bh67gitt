# name = 'Alex'
# age = 35
# print(name, age)
#     ВЫВОД: Alex 35
#
#
# name = 'Alex'
# age = 35
# print(name, age, sep='------')
# print(name, age)
    # ВЫВОД: Alex------35
    # ВЫВОД: Alex 35
#
#
# name = 'Alex'
# age = 35
# print(name, age, end=' finish!')
# print(name, age)
#     ВЫВОД:Alex 35 finish!Alex 35
#
#
# age = input('Enter age: ')
# print(type(age))
#     ВЫВОД: Enter age:
#
#
# a = 456
# print(a)
#     ВЫВОД: 456
#
#
# a = 456
# a +=2
# print(a)
#
#
# text = 'hello world'
# text = text.upper()
# print(text)
#
#
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
#
#
# print(True + True)
# print(False + False)
#
#
# print(float(0))
#
#
# a = 'inf'
# b = 'nan'
# print(float(a))
# print(float(b))
#
#
# print(float('4e34'))
#
#
# a = '1_000_000'
# print(int(a))
#
#
# print(4 / 3)
#
# print(4 // 3)
# print(4 // 3.0)
#
# print(5 % 2)
#
#
# text = 'hello "python" world'
# print(text)
#
# text = 'hello "pyt\'hon" world'
# print(text)
#
# text = 'hello\\ "pyt\'hon" world'
# print(text)
#
#
# name = 'Alex'
# surname = 'Popov'
# fullname = name + surname
# print(fullname)
#
# name = 'Alex'
# surname = 'Popov'
# fullname = name + surname
# print(fullname*2)
#
#
# print(abs(-789456)) # Абсолютное значение
#
#
# print(len('hello world')) # длина строки
#
#
# print(r'C:\Users\Documents')
# print('C:\\Users\\Documents')
# print(r'C:\Users\Documents\n' + '\\')
#
#
# name = 'Alex'
# age = 35
# print('Hello ' + name + ' your age ' + str(35))
#
# print('Hello %s your age %d' % (name, age))
# print('Hello %(first_name)s your age %(user_ahe)d' % ('user_age': age, 'first_name': name))
#
# print('Hello {} your age {}'.format(name, age))
# print('Hello {first_name} your age {user_age}'.format(first_name=name, user_age=age))
#
# print(f'Hello {name} your age {age}')
#
#
# print('\N{fire}')
# print(f'{35} \N{fire}')
# print ('🔥')
#
#
# text = 'hello---world---python'
# print(text.split('---'))
#
# text = 'hello---world---python'
# print(text.split('---', 1))
#
# words = ('word', 'python', 'pycharm')
# text = '---'.join(words)
# print(text)
#
# text = 'hello'
# print('-'.join(text))
#
# text = 'hello python world python'
# print(text.find('python'))
#
# text = 'hello python world python'
# print(text.find('python', 10, 25))
#
#
# text = 'hello python world python pycharm'
# print(text.partition('python'))
# print(text.rpartition('python'))
# print(text.partition('java'))
# print(text.rpartition('java'))
#
#
# text = 'hello world python'
# text = text.replace(' ', '---')
# print(text)
#
#
# print('hello\tpython\tworld\pycharm'.expandtabs(12))
#
#
# text = '.-.-.-.-.,=hello-.,-.=world-=-=-=,.,.,.'
# print(text.lstrip(',.-='))
# print(text.rstrip(',.-='))
# print(text.strip(',.-='))
#
#
# text = 'hello'
# print(text.center(10, '-'))
#
# text = 'hello'
# print(text.center(10))
#
# text = 'hello'
# print(text.ljust(10, '-'))
# print(text.rjust(10, '-'))
# print(text.zfill(10))
#
#
# print(bin(14))
# print(bin(14)[2:])
# print(bin(14)[2:].zfill(8))
#
# text = 'hello'
# print(text.ljust(10, '-').rjust(15, '-'))
#
#
# text = 'Привет мир'
# print(text.encode())
#
# text = 'Hello world'
# print(text.encode())
#
# text = 'Питон'
# print(len(text.encode()))
#
# text = 'Hello'
# print(len(text.encode()))
#
#
# print('hell' in 'world hello python')
#
# print('Hell' in 'world hello python')
#
# print('Hell' not in 'world hello python')
#
#
#
# a = 4
# b = 2+2
# print(a is b)
#
#
# numbers1 = [1, 2, 3]
# numbers2 = [1, 2, 3]
# print(numbers1 is numbers2)
# print(numbers1[0] is numbers2[0])
#
#
# text = 'hello'
# print(not text)
#
#
# a = 13
# b = 15
# print(bin(13))
# print(bin(15))
# print(a & b)
#
# a = 13
# b = 11
# print(bin(13))
# print(bin(11))
# print(a | b)
#
# a = 13
# b = 11
# print(bin(13))
# print(bin(11))
# print(a ^ b)
#
# a = 13
# b = 11
# print(bin(13))
# print(bin(11))
# print(~156)
#
# a = 13
# b = 11
# print(bin(13))
# print(bin(11))
# print(15 << 2)
# print(bin(15 << 2))
# print(13 >> 2)
# print(bin(13 >> 2))
#
#
# n = 128
# print((n & (n - 1) == 0) and n !=0)
#
#
# print(bin(128).count('0'))


