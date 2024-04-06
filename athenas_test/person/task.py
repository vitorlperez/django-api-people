from uuid import UUID
from datetime import  datetime
from typing import List
from .models import Person


class Task: 

    def save(person_dto: Person) -> Person:
        person = Person(
            name=person_dto.name,
            birthdate=person_dto.birthdate,
            cpf=person_dto.cpf,
            sex=person_dto.sex,
            height=person_dto.height,
            weight=person_dto.weight
        )
        person.save()
        return person
    
    def get_one(person_id: UUID) -> Person:
        return Person.objects.get(id=person_id)
    
    def list() -> List[Person]:
        return Person.objects.filter(deleted_at=None)
    
    def search(person_list: List[Person], username: str) -> List[Person]:
        return person_list.filter(name=username)
    
    def update(person: Person, person_dto: dict) -> Person:
        fields_to_update = {}
        for field_name, value in person_dto.items():
            if getattr(person, field_name) != value and value != None:
                fields_to_update[field_name] = value
        
        if not fields_to_update:
            return person
        
        fields_to_update['modified_at'] = datetime.now()
        Person.objects.filter(id=person.id).update(**fields_to_update)
        
        person.refresh_from_db()
        return person
            
    def delete(person) -> None:
        person.deleted_at = datetime.now()
        person.save()