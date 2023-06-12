# # class User(object):
# #
# #     def __init__(self, username, email):
# #         self.username = username
# #         self.email = email
# #
# #     def __str__(self):
# #         return f'User username={self.username} email={self.email}'
# #
# #
# # class Manager(User):
# #
# #     def __init__(self, username, email, salary):
# #         super().__init__(username, email)
# #         self.salary = salary
# #
# #     def dict(self):
# #         return {'username': self.username, 'email': self.email, 'salary': self.salary}
# #
# #
# # class Boss(Manager):
# #
# #     def __init__(self, username, email, salary):
# #         super().__init__(username, email, salary)
# #
# #
# # class A:
# #     name = 'A'
# #
# #
# # class B(A):
# #     name = 'B'
# #
# #
# # class C(A):
# #     pass
# #
# #
# # class D(B, C):
# #     pass
# #
# #
# # # print(D.mro())
#
#
# class User:
#
#     def __init__(self, name):
#         self.name = name
#
#     def dict(self) -> dict:
#         return {'name': self.name}
#
#
# class Manager(User):
#
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#
#     def dict(self):
#         data = super().dict()
#         data.update({'salary': self.salary})
#         return data
#
#
# class DebitCard:
#
#     def __init__(self, card_number, card_name):
#         self.__card_number = card_number
#         self.card_name = card_name
#
#     @property
#     def info(self):
#         return self.card_number + ' ' + self.card_name
#
#     @property
#     def card_number(self):
#         return self.__card_number[:6] + '******' + self.__card_number[-4:]
#
#     @card_number.setter
#     def card_number(self, value):
#         if len(value) != 16:
#             raise ValueError
#         self.__card_number = value
#
#
# class YandexMusic:
#
#     @classmethod
#     def get_music_by_name(cls, name):
#         return name
#
#
# class SpotifyMusic:
#
#     @classmethod
#     def get_music(cls, name):
#         return name
#
#
# class Music:
#
#     @classmethod
#     def get(cls, name, source):
#         if source == 'yandex':
#             return YandexMusic.get_music_by_name(name)
#         elif source == 'spotify':
#             return SpotifyMusic.get_music(name)
#
#
# def get_music(music: YandexMusic | SpotifyMusic):
#     if isinstance(music, YandexMusic):
#         music.get_music_by_name('music')
#     elif isinstance(music, SpotifyMusic):
#         music.get_music('music')
#
#
# class Engine:
#
#     def __init__(self, volume):
#         self.volume = volume
#
#
# class Car:
#
#     def __init__(self, name, engine: Engine):
#         self.engine = engine
#         self.name = name
#
#
# class Manufacture:
#
#     cars = []
#
#     @classmethod
#     def create_cars(cls, count):
#         cars = []
#         for _ in range(count):
#             v8 = Engine(8000)
#             bmw = Car('bawarskoe musornoe wedro', v8)
#             cars.append(bmw)
#             cls.cars.append(bmw)
#         return cars
#
#
# # TODO SOLID
#
#
class Car:

    pass


class FuelCar:

    def zalit_benzin(self):
        pass


class ElectricCar:

    def zaryadit(self):
        pass


class BMW(FuelCar, Car):
    pass


class Tesla(ElectricCar, Car):
    pass


class Toyota(FuelCar, ElectricCar, Car):
    pass


from abc import ABC, abstractmethod


class MusicApi(ABC):

    @classmethod
    @abstractmethod
    def get(cls, music_name: str) -> dict:
        """Get Music By Name
        :param music_name: music name
        :return: response from api
        """


class Yandex(MusicApi):

    @classmethod
    def get(cls, music_name: str) -> dict:
        raise NotImplemented


class MyException(Exception):
    pass