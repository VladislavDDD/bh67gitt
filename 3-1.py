# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами


name = 'Alex'
age = 35
text = 'hello'
text2 = 'world'

print(name, age, text, text2, sep='-')


words = ('Alex', '35', 'hello', 'world')
text = '-'.join(words)
print(text)


text = 'Alex 35 hello world'
text = text.replace(' ', '-')
print(text)