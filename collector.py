import os
from typing import List

from typing import TextIO


class Collector:

    def __init__(self, path):
        self.__path = path
        self.__list_of_files = self.__find_files(self.__path)
        self.__list_of_values = self.__parse_values()

    @property
    def get_list_of_values(self):
        return self.__list_of_values

    @staticmethod
    def __find_files(path: str) -> List[str]:
        return [file for file in os.listdir(path) if file.endswith('spe')]

    @staticmethod
    def __get_cps(file: TextIO) -> int:
        for index, line in enumerate(file):
            if '$CPS:' in line:
                return int(float(file.readline().strip()))

    def __parse_values(self) -> List[int]:
        list_of_values = []
        for file in self.__list_of_files:
            try:
                with open(self.__path + file, 'r') as infile:
                    list_of_values.append(self.__get_cps(infile))
            except FileNotFoundError as err:
                print('{}'.format(err))
        return list_of_values
