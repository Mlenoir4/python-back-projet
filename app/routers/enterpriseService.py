#System imports
from typing import Annotated
from fastapi import Depends


#Libs imports
from fastapi import APIRouter, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

#Local Imports
from model.models import Enterprise, User
from bdd.bdd import enterprise as enterpriseDefaultData, Role
from auth import decode_token, oauth2_scheme, hash_password, JWT_KEY

router = APIRouter()

enterprise = []

def initEnterprise():
    enterprise.extend(enterpriseDefaultData)
    return enterprise



@router.get("/enterprise", response_model_exclude_unset=True)
async def get_all_EnterpriseTypes() -> list[Enterprise]:
    return enterprise


@router.post("/enterprise/create", status_code=status.HTTP_201_CREATED)
async def create_Enterprise(user: Annotated[User, Depends(decode_token)], enterprise: Enterprise):
    if user["role"] != Role.MAINTAINER:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    enterprise.append(enterprise.dict())
    return enterprise


@router.put("/enterprise/update/{Enterprise_id}")
async def update_Enterprise(user: Annotated[User, Depends(decode_token)], Enterprise_id: int, updateEnterprise: Enterprise):
    if user["role"] != Role.MAINTAINER:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    for dataEnterprise in list(filter(lambda x: x["id"] == Enterprise_id, enterprise)):
        dataEnterprise.update(updateEnterprise)
    return enterprise


@router.delete("/enterprise/delete/{Enterprise_id}")
async def delete_Enterprise(user: Annotated[User, Depends(decode_token)], Enterprise_id: int):
    if user["role"] != Role.MAINTAINER:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    for Enterprise in list(filter(lambda x: x["id"] == Enterprise_id, enterprise)):
        Enterprise.pop(Enterprise.index(Enterprise))
    return enterprise
