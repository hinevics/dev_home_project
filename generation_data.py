# NOTE: Написать генератор для таблицы user

# from typing import Any, Tuple
from faker import Faker


class GenerationUser:
    def __init__(self) -> None:
        # initialization Faker
        self.__faker = Faker()
        # initialization data
        self.first_name = self.gen_first_name()
        self.last_name = self.gen_last_name()
        self.email = self.gen_email()
        self.date_birth = self.gen_date_birth()
        # self.phone = gen_phone()

    def gen_last_name(self) -> str:
        return self.__faker.last_name()

    def gen_first_name(self) -> str:
        return self.__faker.first_name()

    def gen_date_birth(self) -> str:
        return self.__faker.date_of_birth(minimum_age=18, maximum_age=50)

    def gen_email(self):
        return self.__faker.free_email()


if __name__ == '__main__':
    g = GenerationUser()
    print(type(g.date_birth))