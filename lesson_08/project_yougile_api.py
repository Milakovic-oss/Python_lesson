import os
import uuid
import requests


class ProjectApi:
    _token = None

    # инициализация
    def __init__(self, url):
        self.url = url

    def headers(self):
        return {"Authorization": "Bearer " + self.get_token()}

    # получить ключ авторизации
    def get_token(self):
        if ProjectApi._token is not None:
            return ProjectApi._token

        env_token = os.getenv("YOUGILE_TOKEN")
        if env_token:
            ProjectApi._token = env_token
            return env_token

        creds = {
            "login": os.getenv("YOUGILE_LOGIN"),
            "password": os.getenv("YOUGILE_PASSWORD"),
            "companyId": os.getenv("YOUGILE_COMPANY_ID"),
        }
        resp = requests.post(self.url + "/auth/keys", json=creds)
        if "key" not in resp.json():
            raise Exception(
                "Авторизация не удалась. Статус: "
                + str(resp.status_code)
                + ". Ответ сервера: "
                + resp.text
            )
        ProjectApi._token = resp.json()["key"]
        return ProjectApi._token

    # создать проект
    def create_project(self, title):
        url_create = self.url + "/projects"
        body = {
            "title": title,
            "idempotencyKey": str(uuid.uuid4())}
        resp = requests.post(
            url_create, json=body, headers=self.headers()
        )
        return resp

    # получить проект по ID
    def get_project(self, project_id):
        url_get = self.url + "/projects/" + project_id
        resp = requests.get(url_get, headers=self.headers())
        return resp

    # изменить проект
    def edit_project(self, project_id, new_title):
        url_edit = self.url + "/projects/" + project_id
        body = {"title": new_title}
        resp = requests.put(
            url_edit, json=body, headers=self.headers()
        )
        return resp
