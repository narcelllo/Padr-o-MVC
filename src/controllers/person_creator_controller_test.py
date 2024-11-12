import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_crate():
    person_info = {
        "first_name": "name",
        "last_name": "last",
        "age": 29,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_crate_error():
    person_info = {
        "first_name": "name@",
        "last_name": "last",
        "age": 29,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
