from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="name", id=4),
            PetsTable(name="name1", id=41),
        ]
    
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "name", "id": 4},
                {"name": "name1", "id": 41}
            ]
        }
    }

    assert response == expected_response 
    