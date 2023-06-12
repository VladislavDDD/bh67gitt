# # file = open('input.txt', 'r', encoding='utf-8')
# #
# #
# # file.close()
#
# # with open('input.txt', 'r', encoding='utf-8') as file:
#     # text = file.read()
#     # print(file.readline())
#     # print(file.readlines())
#     # for line in file:
#     #     pass
#     # file.seek(0)
#     # print(file.read())
#     # print(file.seekable())
# # from time import sleep
# #
# #
# # with open('output.txt', 'w', encoding='utf-8') as file:
# #     for _ in range(10):
# #         file.write('hello\n')
# #         sleep(2)
#
#
# # TODO Дан файл, содержащий в каждой строке числа через пробел
# #  необходимо прочитать файл и для каждой строки посчитать сумму чисел
# #  результат записать в новый файл
#
# # with (
# #     open('input.txt', 'r', encoding='utf-8') as input_file,
# #     open('output.txt', 'w', encoding='utf-8') as output_file
# # ):
# #     for line in input_file:
# #         line = sum([int(number) for number in line.strip().split() if number])
# #         output_file.write(f'{line}\n')
#
#
# # TODO Дан текстовый многострочный файл, для каждой строки в этом файле необходимо
# #  подсчитать количество слов и букв, результат записать в новый файл в формате
# #  В 1 строке 5 слов 15 букв
#
#
# # with (
# #     open('input.txt', 'r', encoding='utf-8') as input_file,
# #     open('output.txt', 'w', encoding='utf-8') as output_file,
# # ):
# #     for i, line in enumerate(input_file):
# #         word_count = (line.strip().count(' ') + 1) if line.strip() else 0
# #         letter_count = len([i for i in line.strip() if i.isalpha()])
# #         output_file.write(f'В строке {i+1} {word_count} слов, {letter_count} букв\n')
#
# # try:
# #     from ujson import load, dump
# # except ModuleNotFoundError:
# #     from json import load, dump
# #
# #
# # with (
# #     open('input.json', 'r', encoding='utf-8') as file,
# #     open('output.json', 'w', encoding='utf-8') as out
# # ):
# #     data = load(file)
# #     data['city'] = 'Минск'
# #     dump(data, out, indent=2, ensure_ascii=False)
#
#
# from csv import reader, writer, DictReader, DictWriter
# #
# #
# # with open('input.csv', 'r', encoding='utf-8') as file:
# #     r = DictReader(file, fieldnames=('name', 'age', 'city'))
# #     for line in r:
# #         print(line)
#     # w = writer(file)
#
#
# # TODO Дан CSV файл необходимо его сериализовать в JSON файл
# from ujson import dump, load
#
#
# with (
#     open('input.csv', 'r', encoding='utf-8') as input_file,
#     open('output.json', 'w', encoding='utf-8') as output_file
# ):
#     dump(
#         [line for line in DictReader(input_file)],
#         output_file,
#         indent=2,
#         ensure_ascii=False
#     )
#
# with (
#     open('output.json', 'r', encoding='utf-8') as input_file,
#     open('output.csv', 'w', encoding='utf-8') as output_file
# ):
#     data = load(input_file)
#     wr = DictWriter(output_file, fieldnames=list(data[0]))
#     wr.writeheader()
#     wr.writerows(data)
# from yaml import safe_load
#
#
# with open('input.yaml', 'r', encoding='utf-8') as file:
#     data = safe_load(file)
# print(data)
# from configparser import ConfigParser
#
# parser = ConfigParser()
# with open('input.ini', 'r', encoding='utf-8') as file:
#     parser.read_file(file)
# from dotenv import load_dotenv
#
# from os import getenv
#
# load_dotenv()
#
# print(getenv('USERNAME'))
from typing import Optional, Union, List, Literal

from pydantic import BaseModel, Field, EmailStr, validator, root_validator
from pydantic.types import Decimal


class RegisterUserForm(BaseModel):
    email: EmailStr = Field(...)
    password: Optional[str] = Field()
    ids: List[Union[str, int]]
    lang_code: Literal['en', 'ru'] = Field(alias='langCode')
    price: Decimal = Field(max_digits=8, decimal_places=2)


class Category(BaseModel):
    name: str = Field(min_length=3, max_length=64)
    parent: Optional["Category"]


Category.update_forward_refs()


users = ['vasya@info.com', 'petya@gmail.com']


import ujson


class User(BaseModel):
    email: EmailStr
    username: str
    password: str

    @validator('email', pre=True)
    def email_validator(cls, value: str) -> str:
        if value in users:
            raise ValueError('email is not unique')
        users.append(value.lower())
        return value.lower()

    @root_validator()
    def validator(cls, values: dict) -> dict:
        if values.get('username').lower() in values.get('password').lower():
            raise ValueError('username has not constraint in password')
        return values

    class Config:
        json_dumps = ujson.dumps
        json_loads = ujson.loads