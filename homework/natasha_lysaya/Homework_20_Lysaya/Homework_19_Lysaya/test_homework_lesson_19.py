import requests
import pytest
import allure


TEST_URL = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def new_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(TEST_URL, json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'{TEST_URL}/{post_id}')
    print('Created object has been deleted')


# ФУНКЦИЯ СОЗДАНИЯ НОВОГО ОБЪЕКТА МЕТОДОМ POST
@allure.feature('Objects')
@allure.story('Post objects')
@allure.title('Создание объекта')
@allure.severity('critical')
@pytest.mark.critical
@pytest.mark.parametrize("objects", [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Dell XPS 13",
        "data": {
            "year": 2020,
            "price": 999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    },
    {
        "name": "HP Spectre x360",
        "data": {
            "year": 2021,
            "price": 1199.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB"
        }
    }
])
def test_create_object(objects, start_end, before_after):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(TEST_URL, json=objects, headers=headers)
    assert response.status_code == 200, f"Incorrect status code {response.status_code}"
    assert response.json()['name'] == objects['name'], f"Incorrect object name {response.json()['name']}"
    assert response.json()['data'] == objects['data'], f"Incorrect object data {response.json()['data']}"
    print(f"Status code {response.status_code}. New created object {response.json()['id']}")


# ФУНКЦИЯ ИЗМЕНЕНИЯ ОБЪЕКТА МЕТОДОМ PUT
@allure.feature('Objects')
@allure.story('Change objects')
@allure.title('Полное изменение объекта')
@allure.severity('normal')
@pytest.mark.medium
def test_change_object_put(new_object, before_after):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{TEST_URL}/{new_object}", json=body, headers=headers)
    assert response.json()['data']['color'] == 'silver'
    print(f"Status code {response.status_code}. Object {response.json()['id']} has been changed")


# ФУНКЦИЯ ИЗМЕНЕНИЯ ОБЪЕКТА МЕТОДОМ PATCH
@allure.feature('Objects')
@allure.story('Change objects')
@allure.title('Частичное изменение объекта')
@allure.severity('normal')
@pytest.mark.medium
def test_change_object_patch(new_object, before_after):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{TEST_URL}/{new_object}", json=body, headers=headers)
    assert response.json()['name'] == "Apple MacBook Pro 16 (Updated Name)"
    print(f"Status code {response.status_code}. Object {response.json()['id']} has been changed")


# ФУНКЦИЯ УДАДЕНИЯ ОБЪЕКТА
@allure.feature('Objects')
@allure.story('Delete objects')
@allure.title('Удаление объекта')
@allure.severity('minor')
@pytest.mark.medium
def test_delete_object(new_object, before_after):
    response = requests.delete(f"{TEST_URL}/{new_object}")
    assert response.status_code == 200, f"Incorrect status code {response.status_code}"
    print(f"Status code {response.status_code}. Required object has been deleted")
