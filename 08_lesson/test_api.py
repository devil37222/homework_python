from ProjectsAPI import ProjectsAPI
from config import MY_API_LOGIN, MY_API_PASSWORD


api = ProjectsAPI(None, "https://ru.yougile.com")


# Проверка получения списка ключей
def test_get_keys():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    resp = api.get_keys_list(login, password)
    resp.json()[0]['key']
    assert resp.status_code == 200


# Проверка создания проекта
def test_create_projectPositiv():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    title = "Старый проект"
    result = api.create_project(title)
    new_id = result.json()['id']
    new_project = api.create_project('new_id')
    assert result.status_code == 201
    assert new_project.json()['id'] != new_id


def test_create_projectNegative():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    result = api.create_project(title="")
    assert result.status_code == 400
    assert 'error' in result.json()


# Провека изменения проекта
def test_update_projectPositiv():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    print(api.get_keys_list(login, password).json()[0]['key'])
    project_id = api.create_project(title="Старый проект").json()['id']
    new_title = "Новый проект"
    result = api.update_project(project_id, new_title)
    assert result.status_code == 200


def test_update_projectNegative():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    project_id = api.create_project(title="Старый проект").json()['id']
    result = api.update_project(project_id, new_title="")
    assert result.status_code == 400
    assert 'error' in result.json()


# Проверка получения проекта по ID
def test_get_project_idPositive():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    project_id = api.create_project(title="Старый проект").json()['id']
    resp = api.get_project_id(project_id)
    assert resp.status_code == 200


def test_get_project_idNegative():
    login = MY_API_LOGIN
    password = MY_API_PASSWORD
    api.get_keys_list(login, password).json()[0]['key']
    project_id = "non_existing_id"
    resp = api.get_project_id(project_id)
    assert resp.status_code == 404
    assert 'error' in resp.json()
