from fastapi import APIRouter
from controllers.authController import registerController
from typing import Any
from models.authModel import RegisterUser 


router = APIRouter(prefix="/api/v1/auth",tags=["auth"])

@router.post("/register")
async def registerView(data:RegisterUser):
    return registerController(data)