# NOTE: Это интефейс работы с базой данных.
# NOTE: находим последнюю запись и добовляет за ней новуюю
# NOTE: также нужен будет интерфейс
# для работы с базой данных, он должен быть общий
from typing import Dict, Union
import datetime

DataTpe = Dict[str, Union[str, int, datetime.date]]


class UserDB:
    def __init__(self, path, temp) -> None:
        # NOTE: Надо Сделать группу переменных которые будут находиться в конфиге
        # NOTE:  Это сделать в виде шаблона для заполнения базы данных
        self.path = path
        self.temp = temp

    @staticmethod
    def parser_data(data: DataTpe):

    def writing_to_db(self, data: DataTpe) -> None:
        data = self.parser_data(data)
        with open(file=self.path, mode='r', encoding='utf-8') as file:


