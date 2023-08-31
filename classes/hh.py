from datetime import datetime

from classes.abstract import AbstractApi
import requests


class HeadHunterApi(AbstractApi):
    base_url = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword

    def get_vacancies(self):
        # Справочник для параметров GET-запроса
        params = {
            'text': f'NAME:{self.keyword}',
            'area': 1,
            'page': 0,          # Номер стартовой страницы поиска
            'per_page': 100      # Количество записей на страницу
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return data.get('items', [])

    @staticmethod
    def list_vacancies(vacancies):
        """ Метод для получения стандартизированного списка вакансий"""
        result = []
        for vacancy in vacancies:
            my_dict = {
                'date': datetime.strptime(vacancy['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d %B %Y'),
                'vacancy': vacancy['name'],
                'company': vacancy['employer']['name'],
                'salary_low': vacancy["salary"]["from"] if vacancy["salary"] else None,
                'salary_top': vacancy['salary']['to'] if vacancy["salary"] else None,
                'employment': vacancy['employment']['name'],
                'url': vacancy['alternate_url'],
                'site': 'headhunter',
            }
            result.append(my_dict)

        return result
