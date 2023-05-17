# From Librairy import the class
from pydantic import BaseModel
from enum import Enum

# From Local import the class

# ip phpMyAdmin = host.docker.internal
class User(BaseModel):
    id: int
    name: str
    role: Enum
    surname: str
    password: str
    age: int
    email: str
    tel: str
    entreprise: int


class Enterprise(BaseModel):
    __id: int
    name: str
    location: str
    email: str
    tel: str


class Activity(BaseModel):
    __id: int
    title: str
    enterprise: int
    user: list[int]
    max_user: int
    inscription: bool = True
    _creation_at: str
    update_at: str
    created_by: int
    start_date: str
    end_date: str
    description: str = None
    city: str = None
    adresse: str = None
    zipCode: str = None
    country: str = None
