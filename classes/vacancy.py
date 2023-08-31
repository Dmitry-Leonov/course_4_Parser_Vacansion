import json
from datetime import datetime

from classes.abstract import AbstractJsonVacancy


class JsonVacancy(AbstractJsonVacancy):
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def get_vacancy(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def len_vacancy(self):
        return len(self.data)

    def print_vacancy(self):
        for file in self.data:
            print(f"Дата публикации объявления {file['date']}")
            print(f"Вакансия: {file['vacancy']}")
            print(f"Компания: {file['company']}")
            print(f"Зарплата: {file['salary_low']} - {file['salary_top']}")
            print(f"Вид занятости {file['employment']}")
            print(f"Ссылка на вакансию {file['url']}")
            print(f"Данная вакансия предоставлена {file['site']}")
            print('-' * 20)

    def add_vacancies(self):
        pass

    def filter_vacancies(self, key_filter):
        result = []
        for i in self.data:
            if i['salary_top'] is None:
                if i['salary_low'] is None:
                    i['salary_top'] = 0
                else:
                    i['salary_top'] = i['salary_low']
            if i['salary_top'] >= int(key_filter):
                result.append(i)
        self.data = result

    def sorted_vacancies(self, key=0):
        if key == '1':
            self.data = sorted(self.data, key=lambda x: datetime.strptime(x['date'], '%d %B %Y'), reverse=True)
        elif key == '2':
            self.data = sorted(self.data, key=lambda x: int(x['salary_top']))
        elif key == '3':
            self.data = sorted(self.data, key=lambda x: int(x['salary_top']), reverse=True)
        else:
            self.data = sorted(self.data, key=lambda x: datetime.strptime(x['date'], '%d %B %Y'))

    def delete_vacancies(self):
        pass
