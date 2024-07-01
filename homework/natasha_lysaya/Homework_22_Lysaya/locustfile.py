from locust import HttpUser, task, between
import random


class ApiUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://api.restful-api.dev"
    stop_timeout = 300
    # А МОЖНО ЕЩЕ ОГРАНИЧИТЬ И ПО КОЛИЧЕСТВУ ИТЕРАЦИЙ,НО ТАМ ЕЩЕ И МЕТОД ПИСАТЬ НАДО))
    # iteration_count = 0
    # max_iterations = 100

    def on_start(self):
        self.headers = {'Content-Type': 'application/json'}

    def create_object(self):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post("/objects", json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()['id']

    def delete_object(self, object_id):
        response = self.client.delete(f"/objects/{object_id}", headers=self.headers)
        response.raise_for_status()

    @task(1)
    def get_random_object(self):
        object_id = self.create_object()
        response = self.client.get(f"/objects/{object_id}", headers=self.headers)
        response.raise_for_status()
        received_object = response.json()
        assert received_object[
            'id'] == object_id, f"Expected object with ID '{object_id}' but got '{received_object['id']}'"
        self.delete_object(object_id)

    @task(2)
    def create_and_verify_object(self):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post("/objects", json=payload, headers=self.headers)
        response.raise_for_status()
        object_id = response.json()['id']
        assert response.json()['name'] == payload['name']
        assert response.json()['data'] == payload['data']
        self.delete_object(object_id)

    @task(3)
    def update_object_put(self):
        object_id = self.create_object()
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        response = self.client.put(f"/objects/{object_id}", json=payload, headers=self.headers)
        response.raise_for_status()
        assert response.json()['data'] == payload['data']
        self.delete_object(object_id)

    @task(4)
    def update_object_patch(self):
        object_id = self.create_object()
        payload = {
            "name": "Apple MacBook Pro 16 (Updated Name)"
        }
        response = self.client.patch(f"/objects/{object_id}", json=payload, headers=self.headers)
        response.raise_for_status()
        assert response.json()['name'] == payload['name']
        self.delete_object(object_id)

    @task(5)
    def delete_object_task(self):
        object_id = self.create_object()
        response = self.client.delete(f"/objects/{object_id}", headers=self.headers)
        response.raise_for_status()
        assert response.status_code in [200], f"Expected status 200 but got {response.status_code}"
        received_response = self.client.get(f"/objects/{object_id}", headers=self.headers)
        assert received_response.status_code == 404, f"Expected status code 404 but got {received_response.status_code}"
