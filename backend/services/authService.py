from config.db import user_collection
async def registerService(data):
    user_dict = data.model_dump()
    await user_collection.insert_one(user_dict)
    if "_id" in user_dict:
        user_dict["_id"] = str(user_dict["_id"])
    return user_dict