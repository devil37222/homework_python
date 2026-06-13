import requests
from config import MY_API_LOGIN, MY_API_PASSWORD


class ProjectsAPI:

    # Инициализация
    def __init__(self, driver, url) -> None:
        self.url = url

    # Получение списка ключей
    def get_keys_list(self, login, password):
        body = {
            "login": login,
             "password": password
            }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=body)
        return resp

    # Создание проекта
    def create_project(self, title):
        login = MY_API_LOGIN
        password = MY_API_PASSWORD
        my_token = self.get_keys_list(login, password).json()[0]['key']
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        project = {
            "title": title
        }
        resp = requests.post(self.url + '/api-v2/projects', json=project,
                             headers=my_headers)
        return resp

    # Изменение проекта
    def update_project(self, id, new_title):
        login = MY_API_LOGIN
        password = MY_API_PASSWORD
        my_token = self.get_keys_list(login, password).json()[0]['key']
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        new_project = {
            "title": new_title
        }
        resp = requests.put(self.url + f'/api-v2/projects/{id}',
                            json=new_project, headers=my_headers)
        return resp

    # Получение проекта по ID
    def get_project_id(self, id):
        login = MY_API_LOGIN
        password = MY_API_PASSWORD
        my_token = self.get_keys_list(login, password).json()[0]['key']
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        resp = requests.get(self.url + f'/api-v2/projects/{id}',
                            headers=my_headers)
        return resp
