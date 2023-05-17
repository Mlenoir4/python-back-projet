# System imports
from typing import Annotated
from fastapi import Depends


# Libs imports
from fastapi import APIRouter, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt


# Local Imports
from model.models import User
from bdd.bdd import users as usersDefaultData
from auth import decode_token, oauth2_scheme, hash_password, JWT_KEY

router = APIRouter()

users = []

#Initialize data for User
def initUsers():
    users.extend(usersDefaultData)
    return users

#Login user
#Return 400 if the user doesn't exist or the password is incorrect
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed_password = hash_password(form_data.password)
    for user in users:
        print(user["name"])
        if user["name"].lower() == form_data.username.lower():
            if hashed_password == user["password"]:
                data = dict()
                data["id"] = user["id"]
                data["name"] = user["name"]
                return {
                    "access_token": jwt.encode(data, JWT_KEY, algorithm="HS256"),
                    "token_type": "bearer"
                }
            break
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Incorrect username or password")

#Get user information by id
#Return 403 if the user try to get information about another user's entreprise
@router.get("/users/{user_id}", response_model_exclude_unset=True, responses={status.HTTP_204_NO_CONTENT: {}})
async def get_user_by_id(user: Annotated[User, Depends(decode_token)], user_id: int):
    data = list(filter(lambda x: x["id"] == user_id, users))
    if user["entreprise"] != data[0]["entreprise"]:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    if len(data) == 0:
        return Response(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return data


#Create new user (name: str, role: Enum, surname: str, password: str, age: int, email: str, tel: str, enterprise: int)
#Return 403 if the user try to create a user for another entreprise
#Only ADMIN can create a new user
@router.post("/users/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: Annotated[User, Depends(decode_token)], newUser: User):
    if user["entreprise"] != newUser.enterprise and user["role"] != "ADMIN":
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    newUser.password = hash_password(newUser.password)
    users.append(newUser.dict())
    return newUser


#Update user information
#Return 403 if the user try to update information about another user's
@router.put("/users/update/{user_id}", tags=["users"], responses={status.HTTP_200_OK : {}})
async def update_user(user: Annotated[User, Depends(decode_token)], user_id: int, updateUser: User):
    if user_id != user["id"]:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    for dataUser in list(filter(lambda x: x["id"] == user_id, users)):
        dataUser.update(updateUser)
    return users


#Delete user
#Return 403 if the user try to delete another user or is not ADMIN for the entreprise
@router.delete("/users/delete/{user_id}", tags=["users"], responses={status.HTTP_406_NOT_ACCEPTABLE: {}})
async def delete_user(user: Annotated[User, Depends(decode_token)], user_id: int):
    data = list(filter(lambda x: x["id"] == user_id, users))
    if user_id != user["id"] or (user["entreprise"] != data[0]["entreprise"] and user["role"] != "ADMIN"):
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    if len(data) == 0:
        return Response(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    for user in data:
        users.pop(users.index(user))
    return users