import pytest

from endpoints.create_object import CreateObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


TEST_DATA = [
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
]

NEGATIVE_DATA = [
    {
        "name": ["My title"],
        "data": {"year": 2019,
                 "price": 1849.99,
                 "CPU model": "Intel Core i9",
                 "Hard disk size": "1 TB"}
    },
    {
        "name": {"My title2": ''},
        "data": {"year": 2020,
                 "price": 999.99,
                 "CPU model": "Intel Core i7",
                 "Hard disk size": "512 GB"}
    }
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(start_end, before_after, data):
    create_obj = CreateObject()
    create_obj.create_new_object(payload=data)
    create_obj.check_that_status_is_200()
    create_obj.check_response_name_is_correct(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_create_object_with_negative_data(start_end, before_after, data):
    create_obj = CreateObject()
    create_obj.create_new_object(payload=data)
    create_obj.check_bad_request()


def test_update_put_object(new_object, before_after):
    update_obj_put = UpdateObjectPut()
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
    update_obj_put.update_object_put(object_id=new_object, payload=payload)
    update_obj_put.check_that_status_is_200()
    update_obj_put.check_response_name_is_correct(payload['name'])


def test_update_patch_object(new_object, before_after):
    update_obj_patch = UpdateObjectPatch()
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    update_obj_patch.update_object_patch(object_id=new_object, payload=payload)
    update_obj_patch.check_that_status_is_200()
    update_obj_patch.check_response_name_is_correct(payload['name'])


def test_delete_object(new_object, before_after):
    delete_obj = DeleteObject()
    delete_obj.delete_object(object_id=new_object)
    delete_obj.check_that_status_is_200()
