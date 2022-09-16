from os import listdir

from os.path import isfile
from os.path import join

from ._kernel import _Singleton


def pdf_from_dir(dir_path):
    pdf_file = tuple()
    for file in listdir(dir_path):
        if file.endswith('.pdf'):
            pdf_file += (file, )
    check = len(pdf_file) >= 1
    return check, pdf_file


class Checker(_Singleton):
    def __filtering(self, key):
        cond_left = self.__data[key].lower().startswith(self.__query)
        cond_right = self.__query == self.__data[key]

        if cond_left or cond_right:
            return True
        return False

    def check(self, query, data):
        self.__query = query.lower()
        self.__data = data.lower()
        condition = self.__query in self.__data
        return condition
