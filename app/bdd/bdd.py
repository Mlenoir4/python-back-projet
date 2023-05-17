from model.models import User, Enterprise, Activity
from enum import Enum


class Role(Enum):
    MAINTAINER = 1
    ADMIN = 2
    USER = 3

users: list[User] = [
    {
        "id": 1,
        "name": "mathieu",
        "role": Role.MAINTAINER,
        "surname": "mathieu",
        "age": 21,
        "email": "leo.D@gmail.com",
        "tel": "06123456789",
        "enterprise": 1,
        "password": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
    },
    {
        "id": 2,
        "name": "admin",
        "role": Role.ADMIN,
        "surname": "Jhonny",
        "age": 12,
        "email": "leo.D@gmail.com",
        "tel": "06123456789",
        "enterprise": 2,
        "password": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
    },
    {
        "id": 3,
        "name": "user",
        "role": Role.USER,
        "surname": "Huguette",
        "age": 25,
        "email": "leo.D@gmail.com",
        "tel": "06123456789",
        "enterprise": 1,
        "password": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
    }
]

activities: list[Activity] = [
        {
            "id": 1,
            "title": "Premiere activite",
            "enterprise": 1,
            "user": [1, 2],
            "max_user": 10,
            "inscription": True,
            "creation_at": "2021-05-01 08:00:00",
            "update_at": "2021-05-01 09:00:00",
            "created_by": 1,
            "start_date": "2021-05-01 10:00:00",
            "end_date": "2021-05-01 12:00:00",
            "description": "Premiere activite",
            "city": "Lyon",
            "adresse": "1 rue de la paix",
            "zipCode": "69001",
            "country": "France"
        },
        {
            "id": 2,
            "title": "deuxieme activite",
            "enterprise": 1,
            "user": [1,3],
            "max_user": 2,
            "inscription": True,
            "creation_at": "2021-05-01 08:00:00",
            "update_at": "2021-05-01 09:00:00",
            "created_by": 1,
            "start_date": "2021-05-01 10:00:00",
            "end_date": "2021-05-01 12:00:00",
            "description": "2eme activite",
            "city": "Lyon",
            "adresse": "1 rue de la paix",
            "zipCode": "69001",
            "country": "France"
        }
    ]


enterprise: list[Enterprise] = [
        {
            "id": 1,
            "name": "Enterprise 1",
            "email": "entreprise1@gmail.com",
            "tel": "06123456789",
            "location": "Lyon"
        },
        {
            "id": 2,
            "name": "Enterprise 2",
            "email": "entreprise2@gmail.com",
            "tel": "06123456789",
            "location": "Lille"
        }
    ]