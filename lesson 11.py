# from datetime import datetime, date, time, timedelta
# from time import sleep
#
#
# # date1 = datetime.now().fromisoformat('2023-05-24T18:59:50.556447')
# # print(date1)
# # print(datetime.fromtimestamp(1684943890.325772))
#
# # print(datetime.now().strftime("%A %d %b %y"))
# # print(datetime.strptime('Wednesday 24 May 23', "%A %d %b %y"))
#
# # register_date = datetime.utcnow()
# # delta = timedelta(weeks=2)
# # end_data = register_date + delta
# # print(end_data)
#
# # while datetime.now() < datetime(year=2023, month=5, day=24, hour=19, minute=10):
# #     sleep(60)
# # print('OK')
# from itertools import *
#
#
# # for i in repeat('hello', 3):  # ['hello', 'hello', 'hello']
# #     print(i)
#
# # print(*permutations('abcd', 2))
# # print(*product('abcd', 'efgh', 'ijkl'))
#
#
# # print(*dropwhile(lambda x: x != 4, [1, 2, 3, 4, 5, 6, 7, 4, 8]))
# # print(*takewhile(lambda x: x != 4, [1, 2, 3, 4, 5, 6, 7, 8]))
#
# # print(*compress([1, 0, 3, 0, 5], [True, False, None, 1]))
#
# # [1, 2, 3, 4, 5]
# # [True, False, None, 1]
#
#
# # for i in islice([1, 2, 3, 4, 5], 1, 4, 1):
# #     print(i)
#
#
# # print(*accumulate([1, 2, 3, 4, 5], lambda x, y: x * y))
# # from math import *
# #
# # print(pow(-4, 0.5))
# # from os import getenv, system
# # from os.path import join
# # from sys import *
# # from pathlib import Path
# #
# #
# # BASE_DIR = Path(__file__).resolve().parent
# # print((BASE_DIR / 'output.txt').is_file())


from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    email: str
    role_id: int


# print(vasya.email)
# print(vasya.__dict__)


from enum import IntEnum
from http import HTTPStatus


class Role(IntEnum):
    ADMIN: int = 1
    MANAGER: int = 2
    USER: int = 3


# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument('-p', '--port', help='ПОРТ', type=int, default=8000)
# parser.add_argument('-d', '--debug', action='store_true', help='ДЕБАГ')
# print(parser.parse_args())


import logging


logging.basicConfig(
    filename='log.log',
    filemode='a',
    level='INFO',
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)

logging.info('Вася зашел на сайт!')
logging.error('У васи неправильно указана почта')