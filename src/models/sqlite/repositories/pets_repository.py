#from typing import List #Python V 3.8 - 
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

class PestsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    #def list_pets(self) -> List: #Python V 3.8 -
    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
