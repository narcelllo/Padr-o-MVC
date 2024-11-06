import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PestsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PestsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)
