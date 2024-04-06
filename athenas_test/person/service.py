from uuid import UUID
from pydantic import validate_arguments
from typing import List
from .models import Person
from .task import Task
from .serializer import PersonSerializer

class PersonService: 

    @validate_arguments
    def add_person(person_dto: PersonSerializer.Create) -> Person:
        return Task.save(person_dto)
    
    @validate_arguments 
    def get_list(username: str = None) -> List[Person]:
        person_list = Task.list()
        if username:
            person_list = Task.search(person_list, username)
        return person_list 
    
    @validate_arguments
    def update(person_id: UUID, person_dto: PersonSerializer.Update) -> Person:
        person = Task.get_one(person_id)
        if person:
           person = Task.update(person, person_dto.dict())
        return person
            
    @validate_arguments
    def delete(person_id: UUID) -> Person:
        person = Task.get_one(person_id)
        if person:
            Task.delete(person)
        return person