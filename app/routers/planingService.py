# System imports
from typing import Annotated
from fastapi import Depends

# Libs imports
from fastapi import APIRouter, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

# Local Imports
from model.models import Activity
from model.models import User
from bdd.bdd import activities as activityDefaultData
from auth import decode_token, oauth2_scheme, hash_password, JWT_KEY

router = APIRouter()

activities = []


def initPlanings():
    activities.extend(activityDefaultData)
    return activities


@router.get("/planing/{user_id}", response_model_exclude_unset=True, responses={status.HTTP_204_NO_CONTENT: {}})
async def get_planing_by_user_id(user: Annotated[User, Depends(decode_token)], user_id: int):
    if user_id != user["id"] or user["role"] not in ["ADMIN", "MAINTAINER"]:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    user_plannings = [x for x in activities if user_id in x['user']]
    return user_plannings


@router.post("/activity/create", status_code=status.HTTP_201_CREATED)
async def create_activity(user: Annotated[User, Depends(decode_token)], activity: Activity):
    if activity.enterprise != user["entreprise"]:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    activities.append(activity.dict())
    return Response(status_code=status.HTTP_200_OK)


@router.patch("/activity/update/{planing_id}", responses={status.HTTP_200_OK : {}})
async def update_activity(user: Annotated[User, Depends(decode_token)], user_id: int, updateActivity: Activity):
    if updateActivity.created_by != user["id"] or updateActivity.enterprise != user["entreprise"]:
        return Response(status_code=status.HTTP_403_FORBIDDEN)
    for dataUser in list(filter(lambda x: x["id"] == user_id, activities)):
        dataUser.update(updateActivity)
    return Response(status_code=status.HTTP_200_OK)


@router.put("/activity/add/{planing_id}", responses={status.HTTP_200_OK : {}})
async def add_user_on_activity(user: Annotated[User, Depends(decode_token)], user_id: int, activity_id: int):
    data = list(filter(lambda x: x["id"] == activity_id, activities))
    if len(data) == 0:
        return Response(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    for activity in data:
        print(activity)
        if activity["created_by"] != user["id"]:
            return Response(status_code=status.HTTP_403_FORBIDDEN)
        activity["user"].append(user_id)
    return Response(status_code=status.HTTP_200_OK)


@router.delete("/activity/delete/{user_id}", responses={status.HTTP_406_NOT_ACCEPTABLE: {}})
async def delete_user_from_activity(user: Annotated[User, Depends(decode_token)], activity_id : int, user_id: int):
    data = list(filter(lambda x: x["id"] == activity_id, activities))
    if len(data) == 0:
        return Response(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    for activity in data:
        print(activity)
        if activity["created_by"] != user["id"]:
            return Response(status_code=status.HTTP_403_FORBIDDEN)
        if user_id in activity["user"]:
            activity["user"].remove(user_id)
    return Response(status_code=status.HTTP_200_OK)
