from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface): 
    def __init__(self, people_repository: PeopleRepositoryInterface) ->None:
        self._people_repository = people_repository

    def faind(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self._people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("People not faind!")
        
        return person
    
    def __format_response(self, person: PeopleTable) -> dict:
        return{
            "data":{
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                }
            }
        }