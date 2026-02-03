from config.Env import ENVConfig
from motor.motor_asyncio import AsyncIOMotorClient
Client = AsyncIOMotorClient(ENVConfig.MONGO_URI)
db=Client[ENVConfig.MONGO_DB]

#use collection
user_collection=db['users']