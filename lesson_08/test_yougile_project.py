import uuid

from project_yougile_api import ProjectApi


URL = "https://ru.yougile.com/api-v2"

# позитивный: проект создается


def test_create_project_positiv():
    api = ProjectApi(URL)
    title = "Проект автотеста" + str(uuid.uuid4())[:8]
    resp = api.create_project(title)
    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert "id" in body, resp.text
    new_id = body["id"]

    got_project = api.get_project(new_id)
    assert got_project.status_code == 200, got_project.text
    assert got_project.json()["title"] == title

# негативный тест: без обязательного title проект не создается


def test_create_project_negative_without_title():
    api = ProjectApi(URL)
    resp = api.create_project(None)
    assert resp.status_code in (400, 422), resp.text

# позитивный: проект создается и читается по ID


def test_get_project_positiv():
    api = ProjectApi(URL)
    title = "Проект для чтения" + str(uuid.uuid4())[:8]
    created = api.create_project(title).json()
    new_id = created["id"]

    resp = api.get_project(new_id)
    assert resp.status_code == 200, resp.text
    assert resp.json()["id"] == new_id
    assert resp.json()["title"] == title

# негативный: несуществующий ID даёт 404


def test_get_project_negative_wrong_id():
    api = ProjectApi(URL)
    fake_id = str(uuid.uuid4())
    resp = api.get_project(fake_id)
    assert resp.status_code == 404, resp.text

# позитивный: название проекта меняется


def test_edit_project_positiv():
    api = ProjectApi(URL)
    old_title = "Старое название" + str(uuid.uuid4())[:8]
    new_title = "Новое название" + str(uuid.uuid4())[:8]
    created = api.create_project(old_title).json()
    new_id = created["id"]

    resp = api.edit_project(new_id, new_title)
    assert resp.status_code == 200, resp.text

    updated = api.get_project(new_id)
    assert updated.status_code == 200, updated.text
    assert updated.json()["title"] == new_title

# негативный: правка несуществуюшего проекта дает 404


def test_edit_project_negative_wrong_id():
    api = ProjectApi(URL)
    fake_id = str(uuid.uuid4())
    resp = api.edit_project(fake_id, "Не должно сработать")
    assert resp.status_code == 404, resp.text
