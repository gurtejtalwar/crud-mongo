from bson import ObjectId
from fastapi import APIRouter
from models.user import User
from config.db import conn

from schemas.user import serializeDict, serializeList
user = APIRouter()

@user.get("/")
async def get_users():
    print(conn.local.user.find())
    print(serializeList(conn.local.user.find()))
    return serializeList(conn.local.user.find())

@user.get("/user/{id}")
async def get_user_by_id(id):
    return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post("/user")
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

@user.put("/user/{id}")
async def update_user(id, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return serializeList(conn.local.user.find_one({"_id": ObjectId(id)})) 

@user.delete("/user/{id}")
async def delete_user(id):
    return conn.local.user.find_one_and_delete({"_id": ObjectId(id)})

