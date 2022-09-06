from os import listdir
from os.path import isfile
from os.path import join

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from ._kernel import _Singleton


def pdf_from_dir(dir_path):
    pdf_file = tuple()
    for file in listdir(dir_path):
        if file.endswith('.pdf'):
            pdf_file += (file, )
    check = len(pdf_file) >= 1
    return check, pdf_file


class Checker(_Singleton):
    def __filtering(self, query, data):
        contains_check = query in data
        extract_same = process.extractOne(query, data.split())
        extract_check = (extract_same[-1] >= 90)

        if contains_check or extract_check:
            return True

    def check(self, query, data):
        return self.__filtering(query.lower(), data.lower())
