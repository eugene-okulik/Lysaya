import requests


# ФУНКЦИЯ СОЗДАНИЯ НОВОГО ОБЪЕКТА МЕТОДОМ POST
def create_object():
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
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200, f"Incorrect status code {response.status_code}"
    assert response.json()['name'] == body['name'], f"Incorrect object name {response.json()['name']}"
    assert response.json()['data'] == body['data'], f"Incorrect object data {response.json()['data']}"
    print("Test 1 passed successfully!")
    print(f"Status code {response.status_code}. New created object {response.json()['id']}")


# МЕТОД ДЛЯ СОЗДАНИЯ НОВОГО ОБЪЕКТА
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
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    return response.json()['id']


# МЕТОД ДЛЯ УДАЛЕНИЯ ОБЪЕКТА
def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


# ФУНКЦИЯ ИЗМЕНЕНИЯ ОБЪЕКТА МЕТОДОМ PUT
def change_object_put():
    post_id = new_object()
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
    response = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=body, headers=headers)
    assert response.json()['data']['color'] == 'silver'
    print("Test 2 passed successfully!")
    print(f"Status code {response.status_code}. Object {response.json()['id']} has been changed")
    clear(post_id)


# ФУНКЦИЯ ИЗМЕНЕНИЯ ОБЪЕКТА МЕТОДОМ PATCH
def change_object_patch():
    post_id = new_object()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=body, headers=headers)
    assert response.json()['name'] == "Apple MacBook Pro 16 (Updated Name)"
    print("Test 3 passed successfully!")
    print(f"Status code {response.status_code}. Object {response.json()['id']} has been changed")
    clear(post_id)


# ФУНКЦИЯ УДАДЕНИЯ ОБЪЕКТА
def delete_object():
    post_id = new_object()
    response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
    print("Test 4 passed successfully!")
    print(f"Status code {response.status_code}. Required object has been deleted")
    print(response.json())


create_object()
change_object_put()
change_object_patch()
delete_object()
