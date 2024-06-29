import pytest

from endpoints.create_object import CreateObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def new_object():
    create_obj = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_obj.create_new_object(payload)
    yield create_obj.object_id
    delete_obj = DeleteObject()
    delete_obj.delete_object(create_obj.object_id)
    print('Created object has been deleted')
