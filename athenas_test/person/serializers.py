from uuid import UUID
from datetime import date
from enum import Enum
from pydantic import BaseModel as PydanticBaseModel
from models import Person


class BaseModel(PydanticBaseModel):
    class Config:
        anystr_strip_whitespace = True
        allow_population_by_field_name = True

class PersonEnum:
    class Sex(str, Enum):
        male: str = 'M'
        female: str = 'F'

class PersonData:
    class Get(BaseModel):
        id: UUID
        name: str
        birthdate: date = None
        cpf: str = None
        sex: PersonEnum.Sex = None
        height: float = None
        weight: float = None

    class Create(BaseModel):
        name: str
        birthdate: date
        cpf: str
        sex: PersonEnum.Sex
        height: float
        weight: float
    
    class Update(BaseModel):
        id: UUID
        name: str = None
        birthdate: date = None
        cpf: str = None
        sex: PersonEnum.Sex = None
        height: float = None
        weight: float = None

    class Delete(BaseModel):
        id: UUID

class PersonSerializer:
    def add_person(self, person_dto: PersonData.Create):
        return Person(
            name=person_dto.name,
            birthdate=person_dto.birthdate,
            cpf=person_dto.cpf,
            sex=person_dto.sex,
            height=person_dto.height,
            weight=person_dto.weight
        )
    def update_person(self, person_dto: PersonData.Update):
        person = Person.objects.filter(pk=person_dto.id)
        if person:
            ...
        
