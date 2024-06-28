import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        self.object_id = self.json.get('id')
        return self.response
