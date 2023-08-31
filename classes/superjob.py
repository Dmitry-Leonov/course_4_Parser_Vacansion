from datetime import datetime
import requests
from classes.abstract import AbstractApi


class SuperJobApi(AbstractApi):

    _id = '2922'
    key = 'v3.r.10450897.d115782447bc498ec5674db31e7c5a112e54add4.797fbfff0eed9546357bb55f7e5074f906b01008'
    base_url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword

    def get_vacancies(self):
        # Справочник для параметров GET-запроса
        params = {
            'keyword': self.keyword,
            'payment_from': 0,
            'count': 100,     # Количество объявлений на страницу
            'page': 0,              # Страница поиска
        }

        response = requests.get(self.base_url, headers={"X-Api-App-Id": self.key}, params=params)
        data = response.json()
        return data.get('objects', [])

    @staticmethod
    def list_vacancies(vacancies):
        """ Метод для получения стандартизированного списка вакансий"""
        result = []
        for vacancy in vacancies:
            my_dict = {
                'date': datetime.fromtimestamp(vacancy['date_published']).strftime('%d %B %Y'),
                'vacancy': vacancy['profession'],
                'company': vacancy['firm_name'],
                'salary_low': vacancy['payment_from'] if vacancy['payment_from'] else None,
                'salary_top': vacancy['payment_to'] if vacancy['payment_to'] else None,
                'employment': vacancy['type_of_work']['title'],
                'url': vacancy['link'],
                'site': 'SuperJob',
            }
            result.append(my_dict)

        return result
