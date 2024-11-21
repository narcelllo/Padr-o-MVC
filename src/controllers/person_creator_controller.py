import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface): 
    def __init__(self, people_repository: PeopleRepositoryInterface) ->None:
        self._people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_lest_name(first_name, last_name)
        self.__inser_person_in_db(first_name, last_name, age, pet_id)
        format_response = self.__format_response(person_info)
        return format_response

    def __validate_first_and_lest_name(self, first_name: str, last_name: str) -> None:
        non_validad_caracteres = re.compile(r'[^a-zA-Z]')

        if non_validad_caracteres.search(first_name) or non_validad_caracteres.search(last_name):
            raise Exception("Invalid name!")
        
    def __inser_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self._people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return{
            "data":{
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }