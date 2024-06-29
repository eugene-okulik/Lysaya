import requests
import allure

from endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):

    @allure.step('Update object with PATCH')
    def update_object_patch(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f"{self.url}/{object_id}", json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
