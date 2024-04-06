from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        anystr_strip_whitespace = True
        allow_population_by_field_name = True

class PersonEnum:
    class Sex(str, Enum):
        male: str = 'M'
        female: str = 'F'

class PersonSerializer:
    class Create(BaseModel):
        name: str
        birthdate: date = None
        cpf: str = None
        sex: PersonEnum.Sex = None
        height: float = None
        weight: float = None
    
    class Update(BaseModel):
        name: str = None
        birthdate: date = None
        cpf: str = None
        sex: PersonEnum.Sex = None
        height: float = None
        weight: float = None