from ProjectsAPI import ProjectsAPI
import os


api = ProjectsAPI(None, "https://ru.yougile.com")


# Проверка получения списка ключей
def test_get_keys():
    login = os.getenv("login")
    password = os.getenv("password")
    resp = api.get_keys_list(login, password)
    resp.json()[0]['key']
    assert resp.status_code == 200


# Проверка создания проекта
def test_create_project():
    login = os.getenv("login")
    password = os.getenv("password")
    api.get_keys_list(login, password).json()[0]['key']
    title = "Старый проект"
    result = api.create_project(title)
    new_id = result.json()['id']
    new_project = api.create_project('new_id')
    assert result.status_code == 201
    assert new_project.json()['id'] != new_id


# Провека изменения проекта
def test_update_project():
    login = os.getenv("login")
    password = os.getenv("password")
    api.get_keys_list(login, password).json()[0]['key']
    project_id = api.create_project(title="Старый проект").json()['id']
    new_title = "Новый проект"
    result = api.update_project(project_id, new_title)
    assert result.status_code == 200


# Проверка получения проекта по ID
def test_get_project_id():
    login = os.getenv("login")
    password = os.getenv("password")
    api.get_keys_list(login, password).json()[0]['key']
    project_id = api.create_project(title="Старый проект").json()['id']
    resp = api.get_project_id(project_id)
    assert resp.status_code == 200
