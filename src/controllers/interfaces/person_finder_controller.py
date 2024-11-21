from abc import ABC, abstractmethod

class PersonFinderControllerInterface(ABC):

    @abstractmethod
    def faind(self, person_id: int) -> dict:
        pass
