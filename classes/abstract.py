from abc import ABC, abstractmethod


class AbstractApi(ABC):
    base_url = ''

    def __init__(self):
        pass

    def get_vacancies(self):
        pass


class AbstractJsonVacancy(ABC):

    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    def print_vacancy(self):
        pass

    @abstractmethod
    def filter_vacancies(self, key):
        pass

    @abstractmethod
    def sorted_vacancies(self):
        pass

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
